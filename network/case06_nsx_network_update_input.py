#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Network function test configration of NSX & vSphere environment.
#


# 要修改网络的ID，该ID可以在network_list的执行结果中找到，或者在web client->logical switch->Summary界面找到
NSX_NETWORK_UPDATE_ID = 'virtualwire-12'


# 要修改的network信息
NSX_NETWORK_UPDATE_REQ_BODY = '''
<virtualWire>
    <name>Test3-LS</name>
    <description>Test3 network for CT</description>
    <tenantId>virtual wire tenant</tenantId>
    <controlPlaneMode>UNICAST_MODE</controlPlaneMode>
</virtualWire>
'''
