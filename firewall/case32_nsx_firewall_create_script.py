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
from case32_nsx_firewall_create_input import *

caseName = 'case32_nsx_firewall_create'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def createFirewall():
    respData = restclient.post(NSX_URL+'/api/4.0/edges', NSX_FIREWALL_CREATE_REQ_BODY, 'createFirewall')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    createFirewall()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())