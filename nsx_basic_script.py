#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for basic function.
# 

import sys
import getopt
import datetime
import libxml2
import ssl
import atexit
import rest

from nsx_basic_input import *

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listTransZones():
    respData = restclient.get(NSX_URL+'/api/2.0/vdn/scopes', 'listTransZones')
    print(restclient.prettyPrint(respData))

def listSpoofGuards():
    respData = restclient.get(NSX_URL+'/api/4.0/services/spoofguard/policies/', 'listSpoofGuards')
    print(restclient.prettyPrint(respData))


# single IP example: 192.168.100.2
def isSingleIp(address):
    return not isIpRange(address)


# IP Range example: 192.168.10.1-192.168.10.2555, or a subnet in CIDR notation (198.168.10.1/24)
def isIpRange(address):
    return address.find('-')>0 or address.find('/')>0


def usage():
    print "Usage:", sys.argv[0], "--api <listTransZones|listSpoofGuards>"


def main():
    apiName = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "?", ["help", "api="])
    except getopt.GetoptError, msg:
        print >> sys.stderr, str(msg)
        usage()
        return 1

    for o, a in opts:
        if o in ("--help", "-?"):
            usage()
            return 0
        elif o == "--api":
            apiName = a
    
    if apiName == "listTransZones":
        listTransZones()

    elif apiName == "listSpoofGuards":
        listSpoofGuards()

    else:
        print "option", apiName, "not recognized"
        usage()
        return 1

    print "NSX API", apiName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())