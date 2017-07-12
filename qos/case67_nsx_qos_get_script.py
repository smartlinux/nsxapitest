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
from case67_nsx_qos_get_input import *

caseName = 'case67_nsx_qos_get'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def getQOS():
    respData = restclient.get("%s/api/4.0/edges/%s/vnics/%s"%(NSX_URL,NSX_EDGE_ID, 
        NSX_EDGE_INTERFACE_INDEX), 'getQOS')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))

    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    ispNodes = xp.xpathEval("//vnic/inShapingPolicy")
    ospNodes = xp.xpathEval("//vnic/outShapingPolicy")
    if len(ispNodes)<1 and len(ospNodes)<1:
        print "[Warning] The interface's QOS policy is not exist."


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    getQOS()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())