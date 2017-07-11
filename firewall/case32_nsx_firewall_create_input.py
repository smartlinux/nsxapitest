#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Firewall function test configration of NSX & vSphere environment.
#

# 创建 edge firewall 的消息体，部分参数取值见下描述:
# datacenterMoid: 通过vSphere MOB找到
# appliance resourcePoolId: edgeVM 所在的cluster ID, 通过vSphere MOB找到 
# appliance datastoreId: edgeVM 所在的datastore ID, 通过vSphere MOB找到
# vnic index: 接口编号，可在 edge->Manage->Settings->Interfaces中找到
# vnic type: 接口类型，取值为 internal or uplink
# vnic portgroupId: 接口所连的portgroup的id，通过vSphere MOB找到
NSX_FIREWALL_CREATE_REQ_BODY = '''
<edge>
  <datacenterMoid>datacenter-2</datacenterMoid>
  <name>ct-edge1</name>
  <description>Description for the edge gateway</description>
  <tenant>wepiao1</tenant>
  <appliances>
    <applianceSize>compact</applianceSize>
    <enableCoreDump>true</enableCoreDump>
    <appliance>
      <resourcePoolId>domain-c7</resourcePoolId>
      <datastoreId>datastore-13</datastoreId>
    </appliance>
  </appliances>
  <vnics>
    <vnic>
      <index>0</index>
      <name>uplink0</name>
      <type>uplink</type>
      <portgroupId>dvportgroup-121</portgroupId>
      <addressGroups>
        <addressGroup>
          <primaryAddress>172.16.100.1</primaryAddress>
          <subnetMask>255.255.255.0</subnetMask>
        </addressGroup>
      </addressGroups>
      <isConnected>true</isConnected>
    </vnic>
  </vnics>
  <cliSettings>
    <userName>admin</userName>
    <password>VMware123456!</password>
    <remoteAccess>false</remoteAccess>
  </cliSettings>
</edge>
'''

