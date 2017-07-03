#!/usr/bin/python
#
# Test script for security group function.
#

import sys
import getopt
import datetime
import rest
import libxml2
import ssl
import atexit

from nsx_basic_input import *
from nsx_securitygroup_input import *

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

SCOPEID = 'globalroot-0'  
#For the scopeId use globalroot-0 for non-universal security groups and universalroot-0 for universal security groups.

restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listSecurityGroup():
    respData = restclient.get(NSX_URL+'/api/2.0/services/securitygroup/scope/'+SCOPEID, 'listSecurityGroup')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'listSecurityGroup')


def getSecurityGroup():
    respData = restclient.get(NSX_URL+'/api/2.0/services/securitygroup/'+NSX_SECURITYGROUP_GET_ID, 'getSecurityGroup')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'getSecurityGroup')


def createSecurityGroup():
    respData = restclient.post(NSX_URL+'/api/2.0/services/securitygroup/'+SCOPEID, 
        NSX_SECURITYGROUP_CREATE_REQ_BODY, 'createSecurityGroup')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'createSecurityGroup')


def updateSecurityGroup():
    respData = restclient.put(NSX_URL+'/api/2.0/services/securitygroup/'+NSX_SECURITYGROUP_UDPATE_ID,
        NSX_SECURITYGROUP_UPDATE_REQ_BODY, 'updateSecurityGroup')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'updateSecurityGroup')


def deleteSecurityGroup():
    respData = restclient.delete(NSX_URL+'/api/2.0/services/securitygroup/'+NSX_SECURITYGROUP_DELETE_ID, 'deleteSecurityGroup')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData), 'deleteSecurityGroup')


def output(msg, caller):
    f = file(datetime.datetime.now().strftime("log/nsx_" + caller + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def usage():
    print "Usage:", sys.argv[0], "--case <createSecurityGroup|listSecurityGroup|getSecurityGroup|updateSecurityGroup|deleteSecurityGroup>"


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
    
    if testcase == "createSecurityGroup":
        createSecurityGroup()

    elif testcase == "listSecurityGroup":
        listSecurityGroup()

    elif testcase == "getSecurityGroup":
        getSecurityGroup()

    elif testcase == "updateSecurityGroup":
        updateSecurityGroup()

    elif testcase == "deleteSecurityGroup":
        deleteSecurityGroup()

    else:
        print "option", testcase, "not recognized"
        usage()
        return 1

    print "NSX API", testcase, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())
