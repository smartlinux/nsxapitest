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
from case62_nsx_securitygrouprule_list_input import *


from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim


caseName = 'case62_nsx_securitygrouprule_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listSecurityGroupRule():
    respData = restclient.get(NSX_URL+'/api/2.0/services/policy/securitypolicy/'+NSX_SECURITYGROUP_GET_ID, 'listSecurityGroupRule')

    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))




def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    listSecurityGroupRule()
    print "NSX API %s completed successfully!"%(caseName)


if __name__ == "__main__":
    sys.exit(main())
