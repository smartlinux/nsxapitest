#!/usr/bin/python
#
# Subnet function test configration of NSX & vSphere environment.
#

# test DLR ID
NSX_SUBNET_EDGE_ID = 'edge-1'


# getSubnet test configuration
NSX_SUBNET_GET_INDEX = '12'


# createSubnet test configuration
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


# deleteSubnet test configuration
NSX_SUBNET_DELETE_INDEX = '12'
