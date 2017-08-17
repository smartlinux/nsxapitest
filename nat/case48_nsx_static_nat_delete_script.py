#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for NAT function.
# Static NAT: 仅用address来映射，不用port来映射

import sys
import datetime
import libxml2

sys.path.append("..")
import rest
from nsx_basic_input import *
from case48_nsx_static_nat_delete_input import *

caseName = 'case48_nsx_static_nat_delete'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def deleteStaticNAT():
    respData = restclient.delete('%s/api/4.0/edges/%s/nat/config/rules/%s'%(NSX_URL,NSX_EDGE_ID, 
        NSX_NAT_RULE_ID), 'deleteStaticNAT')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()   


def main():
    deleteStaticNAT()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())