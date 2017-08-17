#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for firewall function.
# 
# Firewall Policy 映射到 Distributed Firewall Layer3 Section，下面是属性映射关系:
#   防火墙规则ID(rule id)、租户ID(所应用的edge的tenantId)、策略名称(section name)
#   是否共享(所应用的edge的isUniversal)、是否已审计(rule logged)
#

import sys
import datetime
import libxml2

sys.path.append("..")
import rest
from nsx_basic_input import *

caseName = 'case35_nsx_firewall_policy_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listFirewallPolicies():
    respData = restclient.get(NSX_URL+'/api/4.0/firewall/globalroot-0/config?ruleType=LAYER3', 'listFirewallPolicies')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    listFirewallPolicies()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())