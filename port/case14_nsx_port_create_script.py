#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for port function.
# 

import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case14_nsx_port_create_input import *

caseName = 'case14_nsx_port_create'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def createPort():
    respData = restclient.post(NSX_URL+'/api/2.0/vdn/virtualwires/vm/vnic', 
        NSX_PORT_CREATE_REQ_BODY, 'createPort')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    createPort()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())