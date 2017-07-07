#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Router function test configration of NSX & vSphere environment.
#


# NSX Edge ID, 可在web client-> NSX Edges界面找到
NSX_ROUTER_ID = 'edge-7'

# 要增加的接口信息，部分参数取值见下描述:
# vnic type: 接口类型，取值为 internal or uplink
# portgroupId: 接口所连的portgroup的id，通过vSphere MOB找到
NSX_ROUTER_ADDINTERFACE_REQ_BODY = '''
<vnics>
  <vnic>
    <index>2</index>
    <name>internal2</name>
    <addressGroups>
      <addressGroup>
        <primaryAddress>192.168.200.1</primaryAddress>
        <subnetMask>255.255.255.0</subnetMask>
      </addressGroup>
    </addressGroups>
    <mtu>1500</mtu>
    <type>internal</type>
    <isConnected>true</isConnected>
    <portgroupId>dvportgroup-123</portgroupId>
  </vnic>
</vnics>
'''

