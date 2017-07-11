#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for firewall function.
# 
# Firewall rule 映射到 Edge Firewall Rule，下面是属性映射关系:
#   规则ID(firewallRule->id)、租户ID(edge->tenantId)、规则名称(firewallRule->name)、是否共享(isUniversal)
#   防火墙策略ID()、协议类型(service->protocol)、IP协议版本()、源IP地址(source->ipAddress)
#   目的IP地址(destination->ipAddress)、源端口范围(service->sourcePort)、目的端口范围(service->port)、规则动作(action)
#


import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case40_nsx_firewall_rule_list_input import *

caseName = 'case40_nsx_firewall_rule_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listFirewallRules():
    respData = restclient.get('%s/api/4.0/edges/%s/firewall/config'%(NSX_URL,NSX_FIREWALL_ID), 'listFirewallRules')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    listFirewallRules()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())