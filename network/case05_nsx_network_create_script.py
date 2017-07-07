#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for network function.
# 

import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case05_nsx_network_create_input import *

caseName = 'case05_nsx_network_create'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)

def createNetwork():
    respData = restclient.post(NSX_URL+'/api/2.0/vdn/scopes/'+NSX_NETWORK_CREATE_SCOPE_ID+'/virtualwires', 
        NSX_NETWORK_CREATE_REQ_BODY, 'createNetwork')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    createNetwork()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())