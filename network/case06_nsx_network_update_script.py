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
from case06_nsx_network_update_input import *

caseName = 'case06_nsx_network_update'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def updateNetwork():
    respData = restclient.put(NSX_URL+'/api/2.0/vdn/virtualwires/'+NSX_NETWORK_ID,
        NSX_NETWORK_UPDATE_REQ_BODY, 'updateNetwork')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    updateNetwork()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())