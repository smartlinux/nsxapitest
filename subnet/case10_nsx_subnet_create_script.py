#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for subnet function.
# 

import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case10_nsx_subnet_create_input import *

caseName = 'case10_nsx_subnet_create'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def createSubnet():
    respData = restclient.post("%s/api/4.0/edges/%s/vnics?action=patch"%(NSX_URL,NSX_SUBNET_EDGE_ID), 
        NSX_SUBNET_CREATE_REQ_BODY, 'createSubnet')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    createSubnet()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())