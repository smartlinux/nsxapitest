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
from case60_nsx_securitygroup_update_input import *


from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim


caseName = 'case60_nsx_securitygroup_update'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def updateSecurityGroup():
    respData = restclient.put(NSX_URL+'/api/2.0/services/policy/securitypolicy/'+NSX_SECURITYGROUP_UDPATE_ID,
        NSX_SECURITYGROUP_UPDATE_REQ_BODY, 'updateSecurityGroup')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))



def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    updateSecurityGroup()
    print "NSX API %s completed successfully!"%(caseName)


if __name__ == "__main__":
    sys.exit(main())
