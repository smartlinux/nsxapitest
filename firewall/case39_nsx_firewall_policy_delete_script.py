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
from case39_nsx_firewall_policy_delete_input import *

caseName = 'case39_nsx_firewall_policy_delete'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def deleteFirewallPolicy():
    respData = restclient.delete('%s/api/4.0/firewall/globalroot-0/config/layer3sections/%s'%(NSX_URL,
    	NSX_FIREWALL_POLICY_ID), 'deleteFirewallPolicy')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    deleteFirewallPolicy()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())