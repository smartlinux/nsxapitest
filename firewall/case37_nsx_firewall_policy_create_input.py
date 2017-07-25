#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Firewall function test configration of NSX & vSphere environment.
#

# 创建 firewall policy (nsx firewall section) 的消息体
NSX_FIREWALL_POLICY_CREATE_REQ_BODY = '''
<section name="TestSection2">
  <rule disabled="true" logged="true">
    <name>test-1</name>
    <action>ALLOW</action>
  </rule>
  <rule disabled="true" logged="false">
    <name>test-2</name>
    <action>DENY</action>
  </rule>
</section>
'''

