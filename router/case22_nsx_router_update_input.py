#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Router function test configration of NSX & vSphere environment.
#


# NSX Edge ID, 可在web client-> NSX Edges界面找到
NSX_ROUTER_ID = 'edge-7'


# 要改成的名称
NSX_ROUTER_UPDATE_NAME = 'ct-edge9'


# 配置外部网关信息
NSX_ROUTER_UPDATE_DEFAULTROUTE = '''
<staticRouting>
  <staticRoutes/>
  <defaultRoute>
    <description>test default gateway</description>
    <vnic>0</vnic>
    <gatewayAddress>172.16.100.254</gatewayAddress>
    <mtu>1500</mtu>
  </defaultRoute>
</staticRouting>
'''

# 配置NAT
NSX_ROUTER_UPDATE_NAT_CONFIG = '''
<nat>
  <enabled>false</enabled>
  <natRules/>
 </nat>
'''

# NSX_ROUTER_UPDATE_NAT_CONFIG = '''
# <nat>
#   <enabled>true</enabled>
#   <natRules>
#     <natRule>
#       <ruleType>user</ruleType>
#       <action>snat</action>
#       <vnic>0</vnic>
#       <originalAddress>192.168.100.2</originalAddress>
#       <translatedAddress>172.16.100.2</translatedAddress>
#       <loggingEnabled>false</loggingEnabled>
#       <enabled>true</enabled>
#       <description></description>
#       <protocol>any</protocol>
#       <translatedPort>any</translatedPort>
#       <originalPort>any</originalPort>
#     </natRule>
#   </natRules>
# </nat>
# '''
