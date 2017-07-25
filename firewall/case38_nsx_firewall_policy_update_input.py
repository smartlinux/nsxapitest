#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Firewall function test configration of NSX & vSphere environment.
# 在修改Firefall Policy之前，需要用同一ID先执行case36获取该Firewall Policy，从get的结果中取出ETag，
# 并将返回的xml拷入UPDATE_REQ_BODY进行修改，可修改section name, rule name/disabled等等
#

# 需要修改的Firewall Policy ID (NSX Firewall Section ID), 可在list结果里找到
NSX_FIREWALL_POLICY_ID = '1007'

# Get操作返回的ETag
NSX_FIREWALL_POLICY_ETAG = '1500955282840'

# Get操作返回的xml，在此基础上进行修改
NSX_FIREWALL_POLICY_UPDATE_REQ_BODY = '''
<section id="1007" name="TestSection3" type="LAYER3">
  <rule id="1012" disabled="false" logged="true">
    <name>test-3</name>
    <action>allow</action>
    <appliedToList>
      <appliedTo>
        <name>DISTRIBUTED_FIREWALL</name>
        <value>DISTRIBUTED_FIREWALL</value>
        <type>DISTRIBUTED_FIREWALL</type>
        <isValid>true</isValid>
      </appliedTo>
    </appliedToList>
    <sectionId>1007</sectionId>
    <direction>inout</direction>
    <packetType>any</packetType>
  </rule>
  <rule id="1011" disabled="false" logged="false">
    <name>test-4</name>
    <action>allow</action>
    <appliedToList>
      <appliedTo>
        <name>DISTRIBUTED_FIREWALL</name>
        <value>DISTRIBUTED_FIREWALL</value>
        <type>DISTRIBUTED_FIREWALL</type>
        <isValid>true</isValid>
      </appliedTo>
    </appliedToList>
    <sectionId>1007</sectionId>
    <direction>inout</direction>
    <packetType>any</packetType>
  </rule>
</section>
'''

