#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Firewall function test configration of NSX & vSphere environment.
#

# NSX Edge ID, 可在web client-> NSX Edges界面找到
NSX_FIREWALL_ID = 'edge-9'

NSX_FIREWALL_RULE_ID = '131077'

NSX_FIREWALL_RULE_UPDATE_DATA = '''
<firewallRule>
  <name>hehename2</name>
  <enabled>true</enabled>
  <loggingEnabled>false</loggingEnabled>
  <description/>
  <matchTranslated>false</matchTranslated>
  <action>accept</action>
  <source>
    <ipAddress>192.168.100.25</ipAddress>
  </source>
  <destination>
    <ipAddress>172.16.100.25</ipAddress>
  </destination>
  <application>
    <applicationId>application-57</applicationId>
    <applicationId>application-105</applicationId>
    <service>
        <protocol>tcp</protocol>
        <port>5000-5050</port>
        <sourcePort>8000-8050</sourcePort>
      </service>
  </application>
</firewallRule>
'''
