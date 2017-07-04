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
from case07_nsx_network_delete_input import *

caseName = 'case07_nsx_network_delete'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def deleteNetwork():
    respData = restclient.delete(NSX_URL+'/api/2.0/vdn/virtualwires/'+NSX_NETWORK_DELETE_ID, 'deleteNetwork')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    deleteNetwork()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())
