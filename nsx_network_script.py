#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for network function.
# 
# Network map to NSX Logincal Switch, below is attributes mapping relationship:
#   ID(objectId)、名称(name)、管理状态()、状态()、是否共享(isUniversal)、租户ID(tenantId)
#   网络类型(backingType)、物理网络(vdsContextWithBacking)、vlanID(vlanId/vdnId)、qos规则ID(inShapingPolicy/outShapingPolicy/qosTag)
#

import sys
import getopt
import datetime
import libxml2
import ssl
import atexit
import rest

from nsx_basic_input import *
from nsx_network_input import *

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listNetworks():
    respData = restclient.get(NSX_URL+'/api/2.0/vdn/virtualwires', 'listNetworks')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'listNetworks')


def getNetwork():
    respData = restclient.get(NSX_URL+'/api/2.0/vdn/virtualwires/'+NSX_NETWORK_GET_ID, 'getNetwork')
    outputstr = restclient.getDebugInfo() + restclient.prettyPrint(respData)
    
    outputstr += "\nBacking network info by vSphere API:\n"
    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    nodes = xp.xpathEval("//virtualWire/vdsContextWithBacking/backingValue")
    for n in nodes:
        portgroupid = n.content.strip()
        outputstr += getPortGroupInfo(portgroupid)
    output(outputstr, 'getNetwork')


def createNetwork():
    respData = restclient.post(NSX_URL+'/api/2.0/vdn/scopes/'+NSX_NETWORK_CREATE_SCOPE_ID+'/virtualwires', 
        NSX_NETWORK_CREATE_REQ_BODY, 'createNetwork')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'createNetwork')


def updateNetwork():
    respData = restclient.put(NSX_URL+'/api/2.0/vdn/virtualwires/'+NSX_NETWORK_UPDATE_ID,
        NSX_NETWORK_UPDATE_REQ_BODY, 'updateNetwork')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'updateNetwork')


def deleteNetwork():
    respData = restclient.delete(NSX_URL+'/api/2.0/vdn/virtualwires/'+NSX_NETWORK_DELETE_ID, 'deleteNetwork')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'deleteNetwork')


def getPortGroupInfo(portgroupid):
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_NONE
    serviceInstance = SmartConnect(host=VC_IP, user=VC_USER, pwd=VC_PWD, port=443, sslContext=context)
    atexit.register(Disconnect, serviceInstance)
    content = serviceInstance.RetrieveContent()

    dpg_view = content.viewManager.CreateContainerView(content.rootFolder,[vim.dvs.DistributedVirtualPortgroup],True)
    dpgs = [dpg for dpg in dpg_view.view]
    dpg_view.Destroy()

    for dpg in dpgs:
        # print("Found DPG:", dpg.key)
        if dpg.key == portgroupid:
            return str(dpg.config.defaultPortConfig)

    return 'Cannot find portgroup, id: ' + portgroupid


def output(msg, caller):
    f = file(datetime.datetime.now().strftime("log/nsx_" + caller + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def usage():
    print "Usage:", sys.argv[0], "--case <createNetwork|listNetworks|getNetwork|updateNetwork|deleteNetwork>"


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
    
    if testcase == "createNetwork":
        createNetwork()

    elif testcase == "listNetworks":
        listNetworks()

    elif testcase == "getNetwork":
        getNetwork()

    elif testcase == "updateNetwork":
        updateNetwork()

    elif testcase == "deleteNetwork":
        deleteNetwork()

    else:
        print "option", testcase, "not recognized"
        usage()
        return 1

    print "NSX API", testcase, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())
