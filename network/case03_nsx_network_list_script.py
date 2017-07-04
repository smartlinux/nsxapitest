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

sys.path.append("..")
import rest

from nsx_basic_input import *

caseName = 'case03_nsx_network_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listNetworks():
    respData = restclient.get(NSX_URL+'/api/2.0/vdn/virtualwires', 'listNetworks')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    listNetworks()
    print "NSX API %s completed successfully!"%(caseName)

if __name__ == "__main__":
    sys.exit(main())
