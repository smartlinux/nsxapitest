#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Subnet function test configration of NSX & vSphere environment.
#

# DLR ID，可以在web client-> NSX edges里找到
NSX_SUBNET_EDGE_ID = 'edge-1'


# 要创建的subnet信息，其中connectedToId为其所连接的网络ID，该ID可以在network_list的执行结果中找到，或者在web client->logical switch->Summary界面找到
NSX_SUBNET_CREATE_REQ_BODY = '''
<interfaces>
  <interface>
    <name>test-if</name>
    <addressGroups>
      <addressGroup>
        <primaryAddress>192.168.100.1</primaryAddress>
        <subnetMask>255.255.255.0</subnetMask>
      </addressGroup>
    </addressGroups>
    <mtu>1500</mtu>
    <type>internal</type>
    <isConnected>true</isConnected>
    <connectedToId>virtualwire-8</connectedToId>
  </interface>
</interfaces>
'''
