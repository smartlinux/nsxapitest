#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for firewall function.
# 

import sys
import datetime
import libxml2
import StringIO

sys.path.append("..")
import rest

from nsx_basic_input import *
from case38_nsx_firewall_policy_update_input import *

caseName = 'case38_nsx_firewall_policy_update'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def updateFirewallPolicy():
    moreHeaders = ['If-Match: '+NSX_FIREWALL_POLICY_ETAG ]
    respData = restclient.put('%s/api/4.0/firewall/globalroot-0/config/layer3sections/%s'%(NSX_URL, 
    	NSX_FIREWALL_POLICY_ID), NSX_FIREWALL_POLICY_UPDATE_REQ_BODY, 'updateFirewallPolicy', moreHeaders)
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    updateFirewallPolicy()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())