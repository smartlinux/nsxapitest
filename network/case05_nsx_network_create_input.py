#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Network function test configration of NSX & vSphere environment.
#

# TransportZone ID, 该ID值为：执行'python nsx_basic_script.py --case listTransZones'结果中的'vdnScope->objectId'
NSX_NETWORK_CREATE_SCOPE_ID = 'vdnscope-1'


# 要创建的network信息
NSX_NETWORK_CREATE_REQ_BODY = '''
<virtualWireCreateSpec>
    <name>Test2-LS</name>
    <description>Test2 network for CT</description>
    <tenantId>WPtenant</tenantId>
    <controlPlaneMode>UNICAST_MODE</controlPlaneMode>
    <guestVlanAllowed>false</guestVlanAllowed>
</virtualWireCreateSpec>
'''
