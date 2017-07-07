#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for subnet function.
# 

import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *
from case11_nsx_subnet_delete_input import *

caseName = 'case11_nsx_subnet_delete'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def deleteSubnet():
    respData = restclient.delete("%s/api/4.0/edges/%s/interfaces/%s"%(NSX_URL,NSX_SUBNET_EDGE_ID,NSX_SUBNET_DELETE_INDEX), 'deleteSubnet')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    deleteSubnet()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())