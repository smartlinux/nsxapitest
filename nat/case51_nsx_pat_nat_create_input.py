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
    <action>dnat</action>
    <vnic>0</vnic>
    <originalAddress>172.16.200.2</originalAddress>
    <translatedAddress>192.168.200.0/24</translatedAddress>
    <loggingEnabled>false</loggingEnabled>
    <enabled>true</enabled>
    <description>pat nat created by script</description>
    <protocol>any</protocol>
    <translatedPort>any</translatedPort>
    <originalPort>any</originalPort>
  </natRule>
</natRules>
'''