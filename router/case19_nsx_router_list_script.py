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

caseName = 'case19_nsx_router_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listRouters():
    respData = restclient.get(NSX_URL+'/api/4.0/edges', 'listRouters')
    outputstr = restclient.getDebugInfo() + restclient.prettyPrint(respData)

    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    nodes = xp.xpathEval("//pagedEdgeList/edgePage/edgeSummary/objectId")
    
    for node in nodes:
        edgeId = node.content
        outputstr += "\nTry to get router(%s) static and default routes:\n"%(edgeId)
        respData = restclient.get("%s/api/4.0/edges/%s/routing/config/static"%(NSX_URL, edgeId), 'listRouters')
        outputstr += restclient.getDebugInfo() + restclient.prettyPrint(respData)
    
    output(outputstr)


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    listRouters()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())