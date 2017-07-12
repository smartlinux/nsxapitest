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
from case65_nsx_securitygrouprule_delete_input import *


from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim


caseName = 'case65_nsx_securitygrouprule_delete'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def deleteSecurityGroupRule():
    respData = restclient.put(NSX_URL+'/api/2.0/services/policy/securitypolicy/'+NSX_SECURITYGROUP_ID,
        NSX_SECURITYGROUP_UPDATE_REQ_BODY, 'deleteSecurityGroupRule')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))



def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    deleteSecurityGroupRule()
    print "NSX API %s completed successfully!"%(caseName)


if __name__ == "__main__":
    sys.exit(main())
