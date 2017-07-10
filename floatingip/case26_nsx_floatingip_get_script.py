#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for FloatingIP function.
# 
# FloatingIP 映射到 Edge DNAT，下面是属性映射关系:
#   ID(natRule->ruleId)、网络ID(natRule->vnic->portgroupId)、端口ID(natRule->originalPort)、fix_IP地址(natRule->originalAddress)
#   浮动IP(natRule->translatedAddress)、租户ID(edge->tenant)、路由ID(edge->id)、状态(natRule->enabled)
#

import sys
import datetime
import libxml2

sys.path.append("..")
import rest
from nsx_basic_input import *
from case26_nsx_floatingip_get_input import *

caseName = 'case26_nsx_floatingip_get'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def getFloatingIP():
    respData = restclient.get('%s/api/4.0/edges/%s/nat/config'%(NSX_URL,NSX_ROUTER_ID), 'getFloatingIP')
    outputStr = (restclient.getDebugInfo() + restclient.prettyPrint(respData))

    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    rules = xp.xpathEval("//nat/natRules/natRule")

    outputStr += "\n\nFloatingIP(%s) NAT rules:\n"%(NSX_FLOATING_IP)
    for rule in rules:
        xp.setContextNode(rule)
        origAddr = xp.xpathEval("originalAddress")[0].getContent()
        transAddr = xp.xpathEval("translatedAddress")[0].getContent()
        if NSX_FLOATING_IP in [origAddr, transAddr]:
            outputStr += (rule.serialize('UTF-8', 1)+'\n')


    output(outputStr)


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()   


def main():
    getFloatingIP()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())