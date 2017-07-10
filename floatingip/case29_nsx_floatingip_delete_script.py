#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for FloatingIP function.
# 

import sys
import datetime
import libxml2

sys.path.append("..")
import rest
from nsx_basic_input import *
from case29_nsx_floatingip_delete_input import *

caseName = 'case29_nsx_floatingip_delete'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def deleteFloatingIP():
    outputStr = ''
    for ruleId in NSX_NAT_RULE_ID_LIST:
        respData = restclient.delete('%s/api/4.0/edges/%s/nat/config/rules/%s'%(NSX_URL,NSX_ROUTER_ID, ruleId), 'deleteFloatingIP')
        outputStr += (restclient.getDebugInfo() + restclient.prettyPrint(respData))

    output(outputStr)


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()   


def main():
    deleteFloatingIP()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())