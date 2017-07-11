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
from case43_nsx_firewall_rule_update_input import *

caseName = 'case43_nsx_firewall_rule_update'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def updateFirewallRule():
    respData = restclient.put('%s/api/4.0/edges/%s/firewall/config/rules/%s'%(NSX_URL,NSX_FIREWALL_ID,NSX_FIREWALL_RULE_ID),
        NSX_FIREWALL_RULE_UPDATE_DATA, 'updateFirewallRule')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    updateFirewallRule()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())