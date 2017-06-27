#!/usr/bin/python
#
# Network function test configration of NSX & vSphere environment.
#

# getNetwork test case configuration
NSX_NETWORK_GET_ID = 'virtualwire-1'


# createNetwork test case configuration
NSX_NETWORK_CREATE_SCOPE_ID = 'vdnscope-1'
NSX_NETWORK_CREATE_REQ_BODY = '''
<virtualWireCreateSpec>
    <name>Test-LS</name>
    <description>Test network for CT</description>
    <tenantId>WPtenant</tenantId>
    <controlPlaneMode>UNICAST_MODE</controlPlaneMode>
    <guestVlanAllowed>false</guestVlanAllowed>
</virtualWireCreateSpec>
'''


# updateNetwork test case configuration
NSX_NETWORK_UPDATE_ID = 'virtualwire-9'
NSX_NETWORK_UPDATE_REQ_BODY = '''
<virtualWire>
    <name>Test2-LS</name>
    <description>Test2 network for CT</description>
    <tenantId>virtual wire tenant</tenantId>
    <controlPlaneMode>UNICAST_MODE</controlPlaneMode>
</virtualWire>
'''


# deleteNetwork test case configuration
NSX_NETWORK_DELETE_ID = 'virtualwire-9'
