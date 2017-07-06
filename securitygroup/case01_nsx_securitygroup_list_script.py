#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for securitygroup function.
# 


import sys
import datetime
import libxml2
import ssl
import atexit

sys.path.append("..")

import rest

from nsx_basic_input import *


from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

SCOPEID = 'globalroot-0'  
#For the scopeId use globalroot-0 for non-universal security groups and universalroot-0 for universal security groups.
caseName = 'case01_nsx_securitygroup_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listSecurityGroup():
    respData = restclient.get(NSX_URL+'/api/2.0/services/securitygroup/scope/'+SCOPEID, 'listSecurityGroup')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))



def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    listSecurityGroup()
    print "NSX API %s completed successfully!"%(caseName)


if __name__ == "__main__":
    sys.exit(main())