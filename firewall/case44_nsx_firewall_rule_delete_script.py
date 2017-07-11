#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for firewall function.
# 


import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case44_nsx_firewall_rule_delete_input import *

caseName = 'case44_nsx_firewall_rule_delete'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def deleteFirewallRule():
    respData = restclient.delete('%s/api/4.0/edges/%s/firewall/config/rules/%s'%(NSX_URL,NSX_FIREWALL_ID,
    	NSX_FIREWALL_RULE_ID), 'deleteFirewallRule')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    deleteFirewallRule()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())