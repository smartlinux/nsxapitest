#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for NAT function.
# 

import sys
import datetime
import libxml2

sys.path.append("..")
import rest
from nsx_basic_input import *
from nsx_basic_script import isSingleIp, isIpRange
from case45_nsx_static_nat_list_input import *

caseName = 'case45_nsx_static_nat_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listStaticNATs():
    respData = restclient.get('%s/api/4.0/edges/%s/nat/config'%(NSX_URL,NSX_EDGE_ID), 'listStaticNATs')
    outputStr = (restclient.getDebugInfo() + restclient.prettyPrint(respData))

    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    rules = xp.xpathEval("//nat/natRules/natRule")

    outputStr += "\n\nStatic NAT rules:\n"
    for rule in rules:
        xp.setContextNode(rule)
        action = xp.xpathEval("action")[0].getContent()
        origAddr = xp.xpathEval("originalAddress")[0].getContent()
        transAddr = xp.xpathEval("translatedAddress")[0].getContent()
        if isSingleIp(origAddr) and isSingleIp(transAddr):
            outputStr += (rule.serialize('UTF-8', 1)+'\n')

    output(outputStr)


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()   


def main():
    listStaticNATs()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())