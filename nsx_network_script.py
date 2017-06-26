#!/usr/bin/python
#
# Test script for network function.
#

import sys
import getopt
import datetime
import rest

from nsx_basic_input import *
from nsx_network_input import *

restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)

def listNetworks():
    respData = restclient.get(NSX_URL+'/api/2.0/vdn/virtualwires', 'listNetworks')
    output('listNetworks', restclient.getDebugInfo() + restclient.prettyPrint(respData))

def getNetwork():
    respData = restclient.get(NSX_URL+'/api/2.0/vdn/virtualwires/'+NSX_NETWORK_GET_ID, 'getNetwork')
    output('getNetwork', restclient.getDebugInfo() + restclient.prettyPrint(respData))

def createNetwork():
    pass

def updateNetwork():
    pass

def deleteNetwork():
    pass

def output(caller, msg):
    f = file(datetime.datetime.now().strftime("log/nsx_" + caller + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	

def usage():
    """usage()"""
    print "Usage:", sys.argv[0], "--case <createNetwork|listNetworks|getNetwork|updateNetwork|deleteNetwork>"

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
    
    if testcase == "createNetwork":
        createNetwork()

    elif testcase == "listNetworks":
        listNetworks()

    elif testcase == "getNetwork":
        getNetwork()

    elif testcase == "updateNetwork":
        updateNetwork()

    elif testcase == "deleteNetwork":
        deleteNetwork()

    else:
        print "option", testcase, "not recognized"
        usage()
        return 1

    print "NSX API", testcase, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())
