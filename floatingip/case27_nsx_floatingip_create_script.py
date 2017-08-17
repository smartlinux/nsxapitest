#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for FloatingIP function.
# 

import sys
import datetime
import libxml2

sys.path.append("..")
import rest
from nsx_basic_input import *
from case27_nsx_floatingip_create_input import *

caseName = 'case27_nsx_floatingip_create'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def createFloatingIP():
    respData = restclient.post('%s/api/4.0/edges/%s/nat/config/rules'%(NSX_URL,NSX_EDGE_ID), 
        NSX_FLOATINGIP_CREATE_REQ_BODY, 'createFloatingIP')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()   


def main():
    createFloatingIP()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())