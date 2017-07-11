#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# NAT function test configration of NSX & vSphere environment.
#

# NSX Edge ID, 可在web client-> NSX Edges界面找到
NSX_EDGE_ID = 'edge-9'

# 要创建的 NAT 信息
NSX_NAT_CREATE_REQ_BODY = '''
<natRules>
  <natRule>
    <action>snat</action>
    <vnic>0</vnic>
    <originalAddress>192.168.166.0/24</originalAddress>
    <translatedAddress>172.16.166.2</translatedAddress>
    <loggingEnabled>false</loggingEnabled>
    <enabled>true</enabled>
    <description>snat created by script</description>
    <protocol>any</protocol>
    <translatedPort>any</translatedPort>
    <originalPort>any</originalPort>
  </natRule>
</natRules>
'''