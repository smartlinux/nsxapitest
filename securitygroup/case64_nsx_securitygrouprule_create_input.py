#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# SecurityGroup function test configration of NSX & vSphere environment.
#

NSX_SECURITYGROUP_ID = 'policy-7'

# updateSecurityGroup test case configuration


# 先执行case58获取security group（NSX中的security policy），用返回的xml替换下面的值并在此基础上修改
# 为了新增rule，需要添加 <action class="firewallSecurityAction">元素，可拷贝已有的action然后修改, 新增的action不要带objectId
# 本次测试只针对Firewall rules, evison后面的数字可能需要根据实际情况修改，只能大于等于原来的版本号

NSX_SECURITYGROUP_UPDATE_REQ_BODY = '''
<?xml version="1.0" encoding="UTF-8"?>
Put getSecurityPolicy xml result here, then add action element to create rule...
'''


