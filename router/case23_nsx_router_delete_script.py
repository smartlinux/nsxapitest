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
from case23_nsx_router_delete_input import *

caseName = 'case23_nsx_router_delete'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def deleteRouter():
    respData = restclient.delete(NSX_URL+'/api/4.0/edges/'+NSX_ROUTER_ID, 'deleteRouter')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    deleteRouter()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())