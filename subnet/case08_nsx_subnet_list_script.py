#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for subnet function.
# 
# Subnet 映射为 NSX Edge Interface, 下面是属性映射关系:
#   ID(index)、网络ID(portgroupId)、名称(name)，IP版本(4 or 6)、cidr(addressGroup)、网关ip(primaryAddress)
#   使能dhcp(relayAgent)、ipv6地址模式(static)，ipv6_ra模式(static)
#

import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case08_nsx_subnet_list_input import *

caseName = 'case08_nsx_subnet_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listSubnets():
    respData = restclient.get("%s/api/4.0/edges/%s/vnics"%(NSX_URL,NSX_SUBNET_EDGE_ID), 'listSubnets')
    respDebugInfo = restclient.getDebugInfo()

    # output DHCP configuration, which can figure out subnet is DHCP enabled or not
    respData2 = restclient.get("%s/api/4.0/edges/%s/dhcp/config"%(NSX_URL,NSX_SUBNET_EDGE_ID), 'listSubnets')
    respDebugInfo2 = restclient.getDebugInfo()

    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    vnicNodes = xp.xpathEval("//vnics/vnic")

    for vnicNode in vnicNodes:
        xp.setContextNode(vnicNode)
        if xp.xpathEval("isConnected")[0].content == 'false':
            vnicNode.unlinkNode()
            continue

        addressGroups = xp.xpathEval("addressGroups/addressGroup")
        for addressGroup in addressGroups:
            xp.setContextNode(addressGroup)
            if xp.xpathEval("primaryAddress")[0].content.find('.') >0:
                addressGroup.newChild(None, 'ipVersion', '4')
            elif xp.xpathEval("primaryAddress")[0].content.find(':') >0:
                addressGroup.newChild(None, 'ipVersion', '6')
                addressGroup.newChild(None, 'ipv6AddressMode', 'static')
                addressGroup.newChild(None, 'ipv6RaMode', 'static')


    respData = respDoc.serialize('UTF-8', 1)
    outputstr = respDebugInfo + restclient.prettyPrint(respData) + '\n'
    outputstr += respDebugInfo2 + restclient.prettyPrint(respData2) + '\n'
    output(outputstr)


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    listSubnets()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())