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
from case22_nsx_router_update_input import *

caseName = 'case22_nsx_router_update'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def updateRouter():
    # get edge current configuration
    respData = restclient.get(NSX_URL+'/api/4.0/edges/'+NSX_ROUTER_ID, 'getRouter')
    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    xp.xpathEval("//edge/name")[0].setContent(NSX_ROUTER_UPDATE_NAME)

    updateReqData = respDoc.serialize('UTF-8', 1)

    # update router name
    respData = restclient.put(NSX_URL+'/api/4.0/edges/'+NSX_ROUTER_ID, updateReqData, 'updateRouter')
    outputStr = (restclient.getDebugInfo() + restclient.prettyPrint(respData))

    # update router default gateway 
    respData = restclient.put('%s/api/4.0/edges/%s/routing/config/static'%(NSX_URL,NSX_ROUTER_ID),
        NSX_ROUTER_UPDATE_DEFAULTROUTE, 'updateRouter')
    outputStr += (restclient.getDebugInfo() + restclient.prettyPrint(respData))

    # update NAT configuration
    respData = restclient.put('%s/api/4.0/edges/%s/nat/config'%(NSX_URL,NSX_ROUTER_ID),
        NSX_ROUTER_UPDATE_NAT_CONFIG, 'updateRouter')
    outputStr += (restclient.getDebugInfo() + restclient.prettyPrint(respData))

    output(outputStr)


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    updateRouter()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())