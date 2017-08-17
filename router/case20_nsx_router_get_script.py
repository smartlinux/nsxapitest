#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for router function.
# 
# Router map to NSX Edge, below is attributes mapping relationship:
#   ID(objectId)、名称(name)、管理状态(state)、状态(edgeStatus)、租户ID(tenantId)、外部网关(gatewayAddress)
#

import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case20_nsx_router_get_input import *

caseName = 'case20_nsx_router_get'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def getRouter():
    respData = restclient.get(NSX_URL+'/api/4.0/edges/'+NSX_ROUTER_ID, 'getRouter')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    getRouter()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())