#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Subnet function test configration of NSX & vSphere environment.
#

# Edge ID，可以在web client-> NSX edges里找到
NSX_SUBNET_EDGE_ID = 'edge-2'


# 要创建的subnet信息，其中portgroupId为其所连接的网络ID，该ID可以在network_list的执行结果中找到，或者在web client->logical switch->Summary界面找到
NSX_SUBNET_CREATE_REQ_BODY = '''
<vnics>
  <vnic>
    <name>test-if</name>
    <addressGroups>
      <addressGroup>
        <primaryAddress>192.168.100.1</primaryAddress>
        <subnetMask>255.255.255.0</subnetMask>
      </addressGroup>
    </addressGroups>
    <mtu>1500</mtu>
    <type>internal</type>
    <index>9</index>
    <isConnected>true</isConnected>
    <portgroupId>virtualwire-4</portgroupId>
  </vnic>
</vnics>
'''
