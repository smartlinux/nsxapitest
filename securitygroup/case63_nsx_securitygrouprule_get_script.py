#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for securitygroup function.
# 
# ID(action.objectId)、方向(direction)、协议(applicationProtocol)、端口范围(value)、对端IP(secondarySecurityGroup)
# 安全组ID(securityPolicy.objectId)、租户ID(绑定到network时，取network的tenantId)


import sys
import datetime
import libxml2
import ssl
import atexit

sys.path.append("..")

import rest

from nsx_basic_input import *
from case63_nsx_securitygrouprule_get_input import *


from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim


caseName = 'case63_nsx_securitygrouprule_get'
restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)


def getSecurityGroupRule():
    respData = restclient.get(NSX_URL+'/api/2.0/services/policy/securitypolicy/'+NSX_SECURITYGROUP_GET_ID+'/securityactions', 'getSecurityGroupRule')
    respDoc = libxml2.parseDoc(respData)
    xp = respDoc.xpathNewContext()
    found = False
    ruleNodes = xp.xpathEval("//actionsByCategory/action")
    for rule in ruleNodes:
        xp.setContextNode(rule)
        objectId = xp.xpathEval("objectId")[0].getContent()

        if objectId == NSX_RULE_GET_ID:
            found = True
            output(restclient.getDebugInfo() + rule.serialize('UTF-8', 1) + '\n')
            break

    if found == False:
        output(NSX_SECURITYGROUP_GET_ID+':'+NSX_RULE_GET_ID+' is not found\n');


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    getSecurityGroupRule()
    print "NSX API %s completed successfully!"%(caseName)


if __name__ == "__main__":
    sys.exit(main())
