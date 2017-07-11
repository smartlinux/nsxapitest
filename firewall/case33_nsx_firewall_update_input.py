#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Firewall function test configration of NSX & vSphere environment.
#


# NSX Edge ID, 可在web client-> NSX Edges界面找到
NSX_FIREWALL_ID = 'edge-7'


NSX_FIREWALL_UPDATE_DATA = '''
<firewall>
  <enabled>false</enabled>
  <globalConfig>
    <tcpPickOngoingConnections>false</tcpPickOngoingConnections>
    <tcpAllowOutOfWindowPackets>false</tcpAllowOutOfWindowPackets>
    <tcpSendResetForClosedVsePorts>true</tcpSendResetForClosedVsePorts>
    <dropInvalidTraffic>true</dropInvalidTraffic>
    <logInvalidTraffic>false</logInvalidTraffic>
    <tcpTimeoutOpen>30</tcpTimeoutOpen>
    <tcpTimeoutEstablished>21600</tcpTimeoutEstablished>
    <tcpTimeoutClose>30</tcpTimeoutClose>
    <udpTimeout>60</udpTimeout>
    <icmpTimeout>10</icmpTimeout>
    <icmp6Timeout>10</icmp6Timeout>
    <ipGenericTimeout>120</ipGenericTimeout>
    <enableSynFloodProtection>false</enableSynFloodProtection>
  </globalConfig>
  <defaultPolicy>
    <action>deny</action>
    <loggingEnabled>false</loggingEnabled>
  </defaultPolicy>
</firewall>
'''
