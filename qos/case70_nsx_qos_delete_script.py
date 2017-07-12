#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for QOS function.
# 

import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case70_nsx_qos_delete_input import *

caseName = 'case70_nsx_qos_delete'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def deleteQOS():
    respData = restclient.get("%s/api/4.0/edges/%s/vnics/%s"%(NSX_URL,NSX_EDGE_ID, 
        NSX_EDGE_INTERFACE_INDEX), 'getQOS')

    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    vnicNode = xp.xpathEval("//vnic")[0]

    ispNodes = xp.xpathEval("//vnic/inShapingPolicy")
    ospNodes = xp.xpathEval("//vnic/outShapingPolicy")
    if len(ispNodes)<1 and len(ospNodes)<1:
        print "[Warning] The interface's QOS policy have not created."
        return False

    if(len(ispNodes)>0):
        ispNodes[0].unlinkNode()

    if(len(ospNodes)>0):
        ospNodes[0].unlinkNode()

    deleteData = respDoc.serialize('UTF-8', 1)

    respData = restclient.put("%s/api/4.0/edges/%s/vnics/%s"%(NSX_URL,NSX_EDGE_ID, 
        NSX_EDGE_INTERFACE_INDEX), deleteData, 'deleteQOS')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))
    return True


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    if deleteQOS():
        print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())