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
from case09_nsx_subnet_get_input import *

caseName = 'case09_nsx_subnet_get'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def getSubnet():
    respData = restclient.get("%s/api/4.0/edges/%s/interfaces/%s"%(NSX_URL,NSX_SUBNET_EDGE_ID,NSX_SUBNET_GET_INDEX), 'getSubnet')
    outputstr = restclient.getDebugInfo() + restclient.prettyPrint(respData)
    output(outputstr)


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    getSubnet()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())