#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for subnet function.
# 
# Subnet 映射为 NSX DLR Interface, 下面是属性映射关系:
#   ID(index)、网络ID(connectedToId)、名称(name)，IP版本()、cidr(addressGroup)、网关ip(primaryAddress)
#   使能dhcp(relayAgent)、ipv6地址模式()，ipv6_ra模式()
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
    respData = restclient.get("%s/api/4.0/edges/%s/interfaces"%(NSX_URL,NSX_SUBNET_EDGE_ID), 'listSubnets')
    outputstr = restclient.getDebugInfo() + restclient.prettyPrint(respData) + "\n"

    # output DHCP relay configuration, which can figure out subnet is DHCP enabled or not
    respData = restclient.get("%s/api/4.0/edges/%s/dhcp/config/relay"%(NSX_URL,NSX_SUBNET_EDGE_ID), 'listSubnets')
    outputstr += (restclient.getDebugInfo() + restclient.prettyPrint(respData))
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