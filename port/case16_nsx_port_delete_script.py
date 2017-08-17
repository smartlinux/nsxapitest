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
from case16_nsx_port_delete_input import *

caseName = 'case16_nsx_port_delete'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def deletePort():
    respData = restclient.post(NSX_URL+'/api/2.0/vdn/virtualwires/vm/vnic', 
        NSX_PORT_DELETE_REQ_BODY, 'deletePort')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    deletePort()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())