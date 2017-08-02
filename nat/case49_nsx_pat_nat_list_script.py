#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for NAT function.
# PAT NAT: 同时用address和port来映射

import sys
import datetime
import libxml2

sys.path.append("..")
import rest
from nsx_basic_input import *
from nsx_basic_script import isSingleIp, isIpRange
from case49_nsx_pat_nat_list_input import *

caseName = 'case49_nsx_pat_nat_list'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def listPATNATs():
    respData = restclient.get('%s/api/4.0/edges/%s/nat/config'%(NSX_URL,NSX_EDGE_ID), 'listPATNATs')
    outputStr = (restclient.getDebugInfo() + restclient.prettyPrint(respData))

    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    rules = xp.xpathEval("//nat/natRules/natRule")

    outputStr += "\n\nPAT NAT rules:\n"
    for rule in rules:
        xp.setContextNode(rule)
        action = xp.xpathEval("action")[0].getContent()
        origPort = xp.xpathEval("originalPort")[0].getContent()
        transPort = xp.xpathEval("translatedPort")[0].getContent()
        if origPort!='any' or transPort!='any':
            outputStr += (rule.serialize('UTF-8', 1)+'\n')

    output(outputStr)


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()   


def main():
    listPATNATs()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())