#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for subnet function.
# 
# Subnet map to NSX DLR Interface, below is attributes mapping relationship:
#   ID(index)、网络ID(connectedToId)、名称(name)，IP版本、cidr(addressGroup)、网关ip(primaryAddress)
#   使能dhcp(relayAgent)、ipv6地址模式()，ipv6_ra模式()
#

import sys
import getopt
import datetime
import libxml2
import rest

from nsx_basic_input import *
from nsx_subnet_input import *

restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listSubnets():
    respData = restclient.get("%s/api/4.0/edges/%s/interfaces"%(NSX_URL,NSX_SUBNET_EDGE_ID), 'listSubnets')
    outputstr = restclient.getDebugInfo() + restclient.prettyPrint(respData) + "\n"

    # output DHCP relay configuration, which can figure out subnet is DHCP enabled or not
    respData = restclient.get("%s/api/4.0/edges/%s/dhcp/config/relay"%(NSX_URL,NSX_SUBNET_EDGE_ID), 'listSubnets')
    outputstr += (restclient.getDebugInfo() + restclient.prettyPrint(respData))
    output(outputstr, 'listSubnets')


def getSubnet():
    respData = restclient.get("%s/api/4.0/edges/%s/interfaces/%s"%(NSX_URL,NSX_SUBNET_EDGE_ID,NSX_SUBNET_GET_INDEX), 'getSubnet')
    outputstr = restclient.getDebugInfo() + restclient.prettyPrint(respData)
    output(outputstr, 'getSubnet')


def createSubnet():
    respData = restclient.post("%s/api/4.0/edges/%s/interfaces?action=patch"%(NSX_URL,NSX_SUBNET_EDGE_ID), 
        NSX_SUBNET_CREATE_REQ_BODY, 'createSubnet')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'createSubnet')


def deleteSubnet():
    respData = restclient.delete("%s/api/4.0/edges/%s/interfaces/%s"%(NSX_URL,NSX_SUBNET_EDGE_ID,NSX_SUBNET_DELETE_INDEX), 'deleteSubnet')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'deleteSubnet')


def output(msg, caller):
    f = file(datetime.datetime.now().strftime("log/nsx_" + caller + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def usage():
    print "Usage:", sys.argv[0], "--case <createSubnet|listSubnets|getSubnet|deleteSubnet>"


def main():
    testcase = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "?", ["help", "case="])
    except getopt.GetoptError, msg:
        print >> sys.stderr, str(msg)
        usage()
        return 1

    for o, a in opts:
        if o in ("--help", "-?"):
            usage()
            return 0
        elif o == "--case":
            testcase = a
    
    if testcase == "createSubnet":
        createSubnet()

    elif testcase == "listSubnets":
        listSubnets()

    elif testcase == "getSubnet":
        getSubnet()

    elif testcase == "deleteSubnet":
        deleteSubnet()

    else:
        print "option", testcase, "not recognized"
        usage()
        return 1

    print "NSX API", testcase, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())
