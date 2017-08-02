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
from nsx_basic_script import isSingleIp, isIpRange
from case46_nsx_static_nat_get_input import *

caseName = 'case46_nsx_static_nat_get'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def getStaticNAT():
    respData = restclient.get('%s/api/4.0/edges/%s/nat/config'%(NSX_URL,NSX_EDGE_ID), 'getStaticNAT')
    outputStr = (restclient.getDebugInfo() + restclient.prettyPrint(respData))

    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    rules = xp.xpathEval("//nat/natRules/natRule")

    for rule in rules:
        xp.setContextNode(rule)
        action = xp.xpathEval("action")[0].getContent()

        origPort = xp.xpathEval("originalPort")[0].getContent()
        transPort = xp.xpathEval("translatedPort")[0].getContent()
        if NSX_NAT_RULE_ID == xp.xpathEval("ruleId")[0].getContent():
            if origPort=='any' and transPort=='any':
                outputStr += "\n\nStatic NAT rule(%s):\n"%(NSX_NAT_RULE_ID)
                outputStr += (rule.serialize('UTF-8', 1)+'\n')
                output(outputStr)
                return True
            else:
                print "[Error] NAT rule(%s) is not a static rule."%(NSX_NAT_RULE_ID)
                return False
    
    print "[Error] NAT rule(%s) is not exist."%(NSX_NAT_RULE_ID)
    return False
    


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()   


def main():
    if getStaticNAT():
        print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())