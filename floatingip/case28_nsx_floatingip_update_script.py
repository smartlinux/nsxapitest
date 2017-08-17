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
from case28_nsx_floatingip_update_input import *

caseName = 'case28_nsx_floatingip_update'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def updateFloatingIP():
    respData = restclient.put('%s/api/4.0/edges/%s/nat/config/rules/%s'%(NSX_URL,NSX_EDGE_ID, NSX_NAT_RULE_ID), 
        NSX_FLOATINGIP_UPDATE_REQ_BODY, 'updateFloatingIP')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()   


def main():
    updateFloatingIP()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())