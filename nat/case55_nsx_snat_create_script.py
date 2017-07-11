#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for NAT function.
# 

import sys
import datetime
import libxml2

sys.path.append("..")
import rest
from nsx_basic_input import *
from case55_nsx_snat_create_input import *

caseName = 'case55_nsx_snat_create'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def createSNAT():
    respData = restclient.post('%s/api/4.0/edges/%s/nat/config/rules'%(NSX_URL,NSX_EDGE_ID), 
        NSX_NAT_CREATE_REQ_BODY, 'createSNAT')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()   


def main():
    createSNAT()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())