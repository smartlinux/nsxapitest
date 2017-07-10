#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for FloatingIP function.
# 
# FloatingIP 映射到 Edge DNAT，下面是属性映射关系:
#   ID(natRule->ruleId)、网络ID(natRule->vnic->portgroupId)、端口ID(natRule->originalPort)、fix_IP地址(natRule->originalAddress)
#   浮动IP(natRule->translatedAddress)、租户ID(edge->tenant)、路由ID(edge->id)、状态(natRule->enabled)
#

import sys
import datetime
import libxml2

sys.path.append("..")
import rest
from nsx_basic_input import *
from case25_nsx_floatingip_list_input import *

caseName = 'case25_nsx_floatingip_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listFloatingIPs():
    respData = restclient.get('%s/api/4.0/edges/%s/nat/config'%(NSX_URL,NSX_ROUTER_ID), 'listFloatingIPs')
    outputStr = (restclient.getDebugInfo() + restclient.prettyPrint(respData))

    respData = restclient.get('%s/api/4.0/edges/%s'%(NSX_URL,NSX_ROUTER_ID), 'listFloatingIPs')
    outputStr += (restclient.getDebugInfo() + restclient.prettyPrint(respData))

    output(outputStr)


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()   


def main():
    listFloatingIPs()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())