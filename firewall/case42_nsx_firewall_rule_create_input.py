#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Firewall function test configration of NSX & vSphere environment.
#

# NSX Edge ID, 可在web client-> NSX Edges界面找到
NSX_FIREWALL_ID = 'edge-9'

NSX_FIREWALL_RULE_CREATE_DATA = '''
<firewallRules>
  <firewallRule>
    <name>hehename</name>
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
    </application>
  </firewallRule>
</firewallRules>
'''

# NSX_FIREWALL_RULE_CREATE_DATA = '''
# <firewall>
#   <globalConfig>
#     <tcpPickOngoingConnections>false</tcpPickOngoingConnections>
#     <tcpAllowOutOfWindowPackets>false</tcpAllowOutOfWindowPackets>
#     <tcpSendResetForClosedVsePorts>true</tcpSendResetForClosedVsePorts>
#     <dropInvalidTraffic>true</dropInvalidTraffic>
#     <logInvalidTraffic>false</logInvalidTraffic>
#     <tcpTimeoutOpen>30</tcpTimeoutOpen>
#     <tcpTimeoutEstablished>21600</tcpTimeoutEstablished>
#     <tcpTimeoutClose>30</tcpTimeoutClose>
#     <udpTimeout>60</udpTimeout>
#     <icmpTimeout>10</icmpTimeout>
#     <icmp6Timeout>10</icmp6Timeout>
#     <ipGenericTimeout>120</ipGenericTimeout>
#     <enableSynFloodProtection>false</enableSynFloodProtection>
#   </globalConfig>
#   <defaultPolicy>
#     <action>deny</action>
#     <loggingEnabled>false</loggingEnabled>
#   </defaultPolicy>
#   <rules>
#     <rule>
#       <ruleTag>hehetag</ruleTag>
#       <name>hehename</name>
#       <enabled>true</enabled>
#       <loggingEnabled>false</loggingEnabled>
#       <description/>
#       <matchTranslated>false</matchTranslated>
#       <action>accept</action>
#       <source>
#         <ipAddress>192.168.100.25</ipAddress>
#       </source>
#       <destination>
#         <ipAddress>172.16.100.25</ipAddress>
#       </destination>
#       <application>
#         <applicationId>application-57</applicationId>
#       </application>
#     </rule>
#   </rules>
# </firewall>
# '''