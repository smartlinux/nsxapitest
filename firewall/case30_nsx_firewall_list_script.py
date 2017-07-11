#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for firewall function.
# 
# Firewall 映射到 Edge Firewall，下面是属性映射关系:
#   防火墙ID(edgeSummary->objectId)、租户ID(tenantId)、防火墙名称(edgeSummary->name)、
#   管理状态(firewall->enabled)、是否共享(isUniversal)、防火墙策略ID()
#

import sys
import datetime
import libxml2

sys.path.append("..")
import rest
from nsx_basic_input import *

caseName = 'case30_nsx_firewall_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listFirewalls():
    respData = restclient.get(NSX_URL+'/api/4.0/edges', 'listFirewalls')
    outputstr = restclient.getDebugInfo() + restclient.prettyPrint(respData)

    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    nodes = xp.xpathEval("//pagedEdgeList/edgePage/edgeSummary/objectId")
    
    for node in nodes:
        edgeId = node.content
        outputstr += "\n"
        respData = restclient.get("%s/api/4.0/edges/%s/firewall/config"%(NSX_URL, edgeId), 'listFirewalls')
        outputstr += restclient.getDebugInfo() + restclient.prettyPrint(respData)
    
    output(outputstr)


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    listFirewalls()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())