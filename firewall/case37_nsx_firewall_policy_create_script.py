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
from case37_nsx_firewall_policy_create_input import *

caseName = 'case37_nsx_firewall_policy_create'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def createFirewallPolicy():
    respData = restclient.post(NSX_URL+'/api/4.0/firewall/globalroot-0/config/layer3sections', 
    	NSX_FIREWALL_POLICY_CREATE_REQ_BODY, 'createFirewallPolicy')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    createFirewallPolicy()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())