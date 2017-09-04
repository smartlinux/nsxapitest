#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for FloatingIP function.
# 

import sys
import datetime
import libxml2

sys.path.append("..")
import rest
from nsx_basic_input import *
from case27_nsx_floatingip_create_input import *

caseName = 'case27_nsx_floatingip_create'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def createFloatingIP():
    # add nat rules
    respData = restclient.post('%s/api/4.0/edges/%s/nat/config/rules'%(NSX_URL, NSX_EDGE_ID), 
        NSX_FLOATINGIP_CREATE_REQ_BODY, 'createFloatingIP')
    outputstr = (restclient.getDebugInfo() + restclient.prettyPrint(respData))
    
    # enable firewall
    if ENABLE_FIREWALL == 'true':
        respData = restclient.get('%s/api/4.0/edges/%s/firewall/config'%(NSX_URL, NSX_EDGE_ID), 'updateFirewall')
        respDoc = libxml2.parseDoc(respData)
        xp = respDoc.xpathNewContext()
        xp.xpathEval("//firewall/enabled")[0].setContent('true')
        updateData = respDoc.serialize('UTF-8', 1)
        respData = restclient.put('%s/api/4.0/edges/%s/firewall/config'%(NSX_URL, NSX_EDGE_ID), updateData, 'updateFirewall')
        outputstr += (restclient.getDebugInfo() + restclient.prettyPrint(respData))
    
    # add secondary address to unpink interface
    if UNLINK_INDEX != '' and FLOATINGIP_ADDRESS != '':
        respData = restclient.get("%s/api/4.0/edges/%s/vnics/%s"%(NSX_URL,NSX_EDGE_ID, UNLINK_INDEX), 'updateVnicAddr')
        respDoc = libxml2.parseDoc(respData)
        xp = respDoc.xpathNewContext()
        secondaryAddressesNodes = xp.xpathEval("//vnic/addressGroups/addressGroup/secondaryAddresses")
        if len(secondaryAddressesNodes)>0:
            secondaryAddressesNode = secondaryAddressesNodes[0]
            ipAddressNode = secondaryAddressesNode.newChild(None, 'ipAddress', FLOATINGIP_ADDRESS)
        else:
            addressGroupNode = xp.xpathEval("//vnic/addressGroups/addressGroup")[0]
            secondaryAddressesNode = addressGroupNode.newChild(None, 'secondaryAddresses', None)
            ipAddressNode = secondaryAddressesNode.newChild(None, 'ipAddress', FLOATINGIP_ADDRESS)
        updateData = respDoc.serialize('UTF-8', 1)
        respData = restclient.put("%s/api/4.0/edges/%s/vnics/%s"%(NSX_URL,NSX_EDGE_ID, UNLINK_INDEX), updateData, 'updateVnicAddr')
        outputstr += (restclient.getDebugInfo() + restclient.prettyPrint(respData))
    
    output(outputstr)
    
def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()   


def main():
    createFloatingIP()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())