#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for identity function.
# 用户处于已认证状态时，可以正常调用API；而已经注销的用户，则不能成功调用API；默认情况下用户处于已认证状态，调用API操作全程由HTTPS加密
# 


import sys
import datetime
import libxml2

sys.path.append("..")
import rest

from nsx_basic_input import *

caseName = 'case01_nsx_identity_login'
restclient = rest.Rest(NSX_IP, VC_USER, VC_PWD, True)


def userLogin():
    respData = restclient.put('%s/api/2.0/services/usermgmt/user/%s/enablestate/1'%(NSX_URL, NSX_USER),
        '', 'userLogin')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))


def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" + caseName + "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    userLogin()
    print "NSX API", caseName, "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())