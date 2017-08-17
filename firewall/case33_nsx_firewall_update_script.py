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
from case33_nsx_firewall_update_input import *

caseName = 'case33_nsx_firewall_update'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def updateFirewall():
    respData = restclient.put('%s/api/4.0/edges/%s/firewall/config'%(NSX_URL,NSX_FIREWALL_ID),
        NSX_FIREWALL_UPDATE_DATA, 'updateFirewall')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    updateFirewall()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())