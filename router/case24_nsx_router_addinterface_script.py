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
from case24_nsx_router_addinterface_input import *

caseName = 'case24_nsx_router_addinterface'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def addInterface():
    respData = restclient.post('%s/api/4.0/edges/%s/vnics?action=patch'%(NSX_URL, NSX_ROUTER_ID), 
    	NSX_ROUTER_ADDINTERFACE_REQ_BODY, 'addInterface')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    addInterface()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())