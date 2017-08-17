#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for router function.
# 

import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case21_nsx_router_create_input import *

caseName = 'case21_nsx_router_create'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def createRouter():
    respData = restclient.post(NSX_URL+'/api/4.0/edges', NSX_ROUTER_CREATE_REQ_BODY, 'createRouter')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    createRouter()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())