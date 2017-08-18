#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for securitygroup function.
# 
# securitygroup map to NSX security policy, below is attributes mapping relationship:
#   ID(objectId)、名称(name)、租户ID(绑定到network时，取network的tenantId)


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

caseName = 'case57_nsx_securitygroup_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listSecurityGroup():
    respData = restclient.get(NSX_URL+'/api/2.0/services/policy/securitypolicy/all', 'listSecurityGroup')
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
