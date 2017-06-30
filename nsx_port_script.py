#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for port function.
# 
# Port map to vSphere VDS Port, below is attributes mapping relationship:
#   ID(LS.objectId+vm.config.hardware.device.backing.port.portKey)、网络ID(LS.objectId)、名称(LS.name+portKey)、
#   管理状态(vm.guestHeartbeatStatus)、状态(vm.config.hardware.device.connectable.connected)、mac地址(vm.config.hardware.device.macAddress)
#   设备ID(vnicUuid)、租户ID(LS.tenantId)、端口安全使能(spoofguard?)
#   qos规则ID(DPG.config.defaultPortConfig.inShapingPolicy/outShapingPolicy/qosTag)
#

import sys
import getopt
import datetime
import libxml2
import json
import ssl
import atexit
import rest

from nsx_basic_input import *
from nsx_port_input import *

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listPorts():
    respData = restclient.get(NSX_URL+'/api/2.0/vdn/virtualwires', 'listPorts')
    outputstr = restclient.getDebugInfo() + restclient.prettyPrint(respData)

    outputstr += "\nTry to get backing port info by vSphere API:\n"
    dpgMap = getPortGroupMap()
    outputstr += str(dpgMap)

    outputstr += "\n\n\nTry to take out port info from vSphere and NSX API response:\n"
    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    nodes = xp.xpathEval("//virtualWires/dataPage/virtualWire")
    ports = []
    i = 0
    for ls in nodes:
        xp.setContextNode(ls)
        lsId = xp.xpathEval("//virtualWire/objectId")[i].content
        lsName = xp.xpathEval("//virtualWire/name")[i].content
        tenantId = xp.xpathEval("//virtualWire/tenantId")[i].content
        dpgId = xp.xpathEval("//virtualWire/vdsContextWithBacking/backingValue")[i].content
        i += 1

        dpg = dpgMap[dpgId]
        if dpg == None:
            continue;

        for vm in dpg.vm:
            for dev in vm.config.hardware.device:
                if isinstance(dev, vim.vm.device.VirtualEthernetCard):
                    if dev.connectable.connected:
                        port = {}
                        port['id'] = "%s.%s"%(lsId, dev.backing.port.portKey)
                        port['networkid'] = lsId
                        port['name'] = "%s.%s"%(lsName, dev.backing.port.portKey)
                        port['mgmtState'] = vm.guestHeartbeatStatus
                        port['state'] = 'connected' if dev.connectable.connected else 'disconnected'
                        port['macAddress'] = dev.macAddress
                        port['deviceid'] = "%s.%s"%(vm.config.instanceUuid, str(dev.key)[-3:])
                        port['tenantId'] = tenantId
                        port['enablesecurity'] = False
                        port['qosTag'] = dpg.config.defaultPortConfig.qosTag.value
                        ports.append(port)
    
    outputstr += json.dumps(ports, sort_keys=True, indent=4, separators=(',',': '))
    output(outputstr, 'listPorts')
    return True


def getPort():
    # get lsId and portKey from input parameter NSX_PORT_GET_ID
    pids = NSX_PORT_GET_ID.split('.')
    if len(pids) != 2:
        print "[Error] NSX_PORT_ID:%s is wrong format."%(NSX_PORT_GET_ID)
        return False
    lsId = pids[0]
    portKey = pids[1]

    # get ls object by NSX API
    respData = restclient.get(NSX_URL+'/api/2.0/vdn/virtualwires/'+lsId, 'getPort')
    outputstr = restclient.getDebugInfo() + restclient.prettyPrint(respData)

    # get port group list by vSphere API
    outputstr += "\nTry to get backing port info by vSphere API:\n"
    dpgMap = getPortGroupMap()
    outputstr += str(dpgMap)
    
    
    outputstr += "\n\n\nTry to take out port info from vSphere and NSX API response:\n"
    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    lsName = xp.xpathEval("//virtualWire/name")[0].content
    tenantId = xp.xpathEval("//virtualWire/tenantId")[0].content
    dpgId = xp.xpathEval("//virtualWire/vdsContextWithBacking/backingValue")[0].content

    dpg = dpgMap[dpgId]
    if dpg == None:
        print "[Error] NSX_DPG_ID:%s not found."%(dpgId)
        return False

    
    # try to find connected port in all the attached vms by portKey
    for vm in dpg.vm:
        for dev in vm.config.hardware.device:
            if isinstance(dev, vim.vm.device.VirtualEthernetCard):
                if dev.connectable.connected and portKey==dev.backing.port.portKey:
                    port = {}
                    port['id'] = "%s.%s"%(lsId, portKey)
                    port['networkid'] = lsId
                    port['name'] = "%s.%s"%(lsName, portKey)
                    port['tenantId'] = tenantId
                    port['enablesecurity'] = False
                    port['qosTag'] = dpg.config.defaultPortConfig.qosTag.value
                    port['mgmtState'] = vm.guestHeartbeatStatus
                    port['state'] = 'connected' if dev.connectable.connected else 'disconnected'
                    port['macAddress'] = dev.macAddress
                    port['deviceid'] = "%s.%s"%(vm.config.instanceUuid, str(dev.key)[-3:])
                    outputstr += json.dumps(port, sort_keys=True, indent=4, separators=(',',': '))
                    output(outputstr, 'getPort')
                    return True
    
    print "[Error] NSX_PORT_ID:%s not found."%(NSX_PORT_GET_ID)
    return False    
    


def createPort():
    respData = restclient.post(NSX_URL+'/api/2.0/vdn/virtualwires/vm/vnic', 
        NSX_PORT_CREATE_REQ_BODY, 'createPort')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'createPort')
    return True


def deletePort():
    respData = restclient.post(NSX_URL+'/api/2.0/vdn/virtualwires/vm/vnic', 
        NSX_PORT_DELETE_REQ_BODY, 'deletePort')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'deletePort')
    return True


def getPortGroupMap():
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_NONE
    serviceInstance = SmartConnect(host=VC_IP, user=VC_USER, pwd=VC_PWD, port=443, sslContext=context)
    atexit.register(Disconnect, serviceInstance)
    content = serviceInstance.RetrieveContent()

    dpg_view = content.viewManager.CreateContainerView(content.rootFolder,[vim.dvs.DistributedVirtualPortgroup],True)
    dpgs = [dpg for dpg in dpg_view.view]
    dpg_view.Destroy()
    dpgMap = {}
    for dpg in dpgs:
        dpgMap[dpg.key] = dpg
    return dpgMap


def output(msg, caller):
    f = file(datetime.datetime.now().strftime("log/nsx_" + caller + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def usage():
    print "Usage:", sys.argv[0], "--case <createPort|listPorts|getPort|deletePort>"


def main():
    testcase = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "?", ["help", "case="])
    except getopt.GetoptError, msg:
        print >> sys.stderr, str(msg)
        usage()
        return 1

    for o, a in opts:
        if o in ("--help", "-?"):
            usage()
            return 0
        elif o == "--case":
            testcase = a
    
    ret = True
    if testcase == "createPort":
        ret = createPort()

    elif testcase == "listPorts":
        ret = listPorts()

    elif testcase == "getPort":
        ret = getPort()

    elif testcase == "deletePort":
        ret = deletePort()

    else:
        print "option", testcase, "not recognized"
        usage()
        return 1

    if ret:
        print "NSX API", testcase, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())
