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
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'listNetworks')


def getNetwork():
    respData = restclient.get(NSX_URL+'/api/2.0/vdn/virtualwires/'+NSX_NETWORK_GET_ID, 'getNetwork')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'getNetwork')


def createNetwork():
    respData = restclient.post(NSX_URL+'/api/2.0/vdn/scopes/'+NSX_NETWORK_CREATE_SCOPE_ID+'/virtualwires', 
        NSX_NETWORK_CREATE_REQ_BODY, 'createNetwork')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'createNetwork')


def updateNetwork():
    respData = restclient.put(NSX_URL+'/api/2.0/vdn/virtualwires/'+NSX_NETWORK_UPDATE_ID,
        NSX_NETWORK_UPDATE_REQ_BODY, 'updateNetwork')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'updateNetwork')


def deleteNetwork():
    respData = restclient.delete(NSX_URL+'/api/2.0/vdn/virtualwires/'+NSX_NETWORK_DELETE_ID, 'deleteNetwork')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'deleteNetwork')


def output(msg, caller):
    f = file(datetime.datetime.now().strftime("log/nsx_" + caller + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def usage():
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
