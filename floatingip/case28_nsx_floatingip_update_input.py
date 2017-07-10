#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# FloatingIP function test configration of NSX & vSphere environment.
#

# NSX Edge ID, 可在web client-> NSX Edges界面找到
NSX_ROUTER_ID = 'edge-7'

# 要修改的floatingIP所对应的nat ruleID
NSX_NAT_RULE_ID = '196613'

# 要创建的 floatingIP 信息
NSX_FLOATINGIP_UPDATE_REQ_BODY = '''
<natRule>
  <action>dnat</action>
  <vnic>0</vnic>
  <originalAddress>172.16.100.2</originalAddress>
  <translatedAddress>192.168.100.20</translatedAddress>
  <loggingEnabled>false</loggingEnabled>
  <enabled>true</enabled>
  <description>wawa</description>
  <protocol>tcp</protocol>
  <translatedPort>80</translatedPort>
  <originalPort>80</originalPort>
</natRule>
'''