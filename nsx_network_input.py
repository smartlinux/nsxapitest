#!/usr/bin/python
#
# Network function test configration of NSX & vSphere environment.
#

# getNetwork test case configuration
NSX_NETWORK_GET_ID = 'virtualwire-5'


# createNetwork test case configuration
NSX_NETWORK_CREATE_SCOPE_ID = 'vdnscope-1'
NSX_NETWORK_CREATE_REQ_BODY = '''
<virtualWireCreateSpec>
    <name>Web-Tier-01</name>
    <description>Web tier network</description>
    <tenantId>WPtenant</tenantId>
    <controlPlaneMode>UNICAST_MODE</controlPlaneMode>
    <guestVlanAllowed>false</guestVlanAllowed>
</virtualWireCreateSpec>
'''


# updateNetwork test case configuration
NSX_NETWORK_UPDATE_ID = 'virtualwire-5'
NSX_NETWORK_UPDATE_REQ_BODY = '''
<virtualWire>
    <name>ULS-Web-Tier-02 </name>
    <description>Universal Web Logical Switch</description>
    <tenantId>virtual wire tenant</tenantId>
    <controlPlaneMode>UNICAST_MODE</controlPlaneMode>
</virtualWire>
'''


# deleteNetwork test case configuration
NSX_NETWORK_DELETE_ID = 'virtualwire-5'
