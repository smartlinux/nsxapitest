#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# FloatingIP function test configration of NSX & vSphere environment.
#

# NSX Edge ID, 可在web client-> NSX Edges界面找到
NSX_ROUTER_ID = 'edge-7'

# 要创建的 floatingIP 信息
NSX_FLOATINGIP_CREATE_REQ_BODY = '''
<natRules>
  <natRule>
    <action>dnat</action>
    <vnic>0</vnic>
    <originalAddress>172.16.100.2</originalAddress>
    <translatedAddress>192.168.100.2</translatedAddress>
    <loggingEnabled>false</loggingEnabled>
    <enabled>true</enabled>
    <description>hehe</description>
    <protocol>any</protocol>
    <translatedPort>any</translatedPort>
    <originalPort>any</originalPort>
  </natRule>
  <natRule>
    <action>dnat</action>
    <vnic>0</vnic>
    <originalAddress>172.16.100.3</originalAddress>
    <translatedAddress>192.168.100.3</translatedAddress>
    <loggingEnabled>false</loggingEnabled>
    <enabled>true</enabled>
    <description>hehe</description>
    <protocol>any</protocol>
    <translatedPort>any</translatedPort>
    <originalPort>any</originalPort>
  </natRule>
</natRules>
'''