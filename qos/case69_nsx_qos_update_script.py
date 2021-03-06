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
from case69_nsx_qos_update_input import *

caseName = 'case69_nsx_qos_update'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def updateQOS():
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

    newIspNode = vnicNode.newChild(None, 'inShapingPolicy', None)
    newIspNode.newChild(None, 'averageBandwidth', inShapingPolicy_averageBandwidth)
    newIspNode.newChild(None, 'peakBandwidth', inShapingPolicy_peakBandwidth)
    newIspNode.newChild(None, 'enabled', inShapingPolicy_enabled)
    newIspNode.newChild(None, 'burstSize', '0')
    newIspNode.newChild(None, 'inherited', 'false')

    newOspNode = vnicNode.newChild(None, 'outShapingPolicy', None)
    newOspNode.newChild(None, 'averageBandwidth', outShapingPolicy_averageBandwidth)
    newOspNode.newChild(None, 'peakBandwidth', outShapingPolicy_peakBandwidth)
    newOspNode.newChild(None, 'enabled', outShapingPolicy_enabled)
    newOspNode.newChild(None, 'burstSize', '0')
    newOspNode.newChild(None, 'inherited', 'false')

    updateData = respDoc.serialize('UTF-8', 1)

    respData = restclient.put("%s/api/4.0/edges/%s/vnics/%s"%(NSX_URL,NSX_EDGE_ID, 
        NSX_EDGE_INTERFACE_INDEX), updateData, 'updateQOS')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))
    return True


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    if updateQOS():
        print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())