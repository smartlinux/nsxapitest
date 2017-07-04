#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for network function.
# 
# Network 映射为 NSX Logincal Switch, 下面是属性映射关系:
#   ID(objectId)、名称(name)、管理状态()、状态()、是否共享(isUniversal)、租户ID(tenantId)
#   网络类型(backingType)、物理网络(vdsContextWithBacking)、vlanID(vlanId/vdnId)、qos规则ID(inShapingPolicy/outShapingPolicy/qosTag)
#

import sys
import datetime
import libxml2
import ssl
import atexit

sys.path.append("..")
import rest

from nsx_basic_input import *
from case04_nsx_network_get_input import *

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

caseName = 'case04_nsx_network_get'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


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
    output(outputstr)


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


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    getNetwork()
    print "NSX API %s completed successfully!"%(caseName)


if __name__ == "__main__":
    sys.exit(main())
