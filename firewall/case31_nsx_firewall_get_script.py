#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for firewall function.
# 
# Firewall 映射到 Edge Firewall，下面是属性映射关系:
#   防火墙ID(edgeSummary->objectId)、租户ID(tenantId)、防火墙名称(edgeSummary->name)、
#   管理状态(firewall->enabled)、是否共享(isUniversal)、防火墙策略ID()
#


import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case31_nsx_firewall_get_input import *

caseName = 'case31_nsx_firewall_get'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def getFirewall():
    respData = restclient.get(NSX_URL+'/api/4.0/edges/'+NSX_FIREWALL_ID, 'getFirewall')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    getFirewall()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())