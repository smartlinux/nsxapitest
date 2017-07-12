#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for QOS function.
# 
# QOS 映射到 Edge interface shaping policy ，下面是属性映射关系:
#   ID(label)、租户ID(可在edge层面查到)、名称(name)、是否共享(inherited)
#

import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case66_nsx_qos_list_input import *

caseName = 'case66_nsx_qos_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listQOS():
    outputStr = ''
    for edgeId in NSX_EDGE_ID_LIST:
        respData = restclient.get("%s/api/4.0/edges/%s/vnics"%(NSX_URL,edgeId), 'listQOS')

        respDoc = libxml2.parseDoc(respData)
        xp = respDoc.xpathNewContext()
        vnicNodes = xp.xpathEval("//vnics/vnic")
        for vnicNode in vnicNodes:
            xp.setContextNode(vnicNode)
            ispNodes = xp.xpathEval("inShapingPolicy")
            ospNodes = xp.xpathEval("outShapingPolicy")
            if len(ispNodes)==0 and len(ospNodes)==0:
                vnicNode.unlinkNode()
        outputStr += (restclient.getDebugInfo() + respDoc.serialize('UTF-8', 1) + '\n')

    print(outputStr)

def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    listQOS()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())