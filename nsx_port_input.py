#!/usr/bin/python
#
# Port function test configration of NSX & vSphere environment.
#

# getPort test case configuration
NSX_PORT_GET_ID = 'virtualwire-3.41'


# createPort test case configuration
# Use these two values to form the VM vNIC ID. For example, if the instanceUuid is
# 502e71fa-1a00-759b-e40f-ce778e915f16 and the appropriate device value is device[4000], the objectId and
# vnicUuid are both 502e71fa-1a00-759b-e40f-ce778e915f16.000.
NSX_PORT_CREATE_REQ_BODY = '''
<com.vmware.vshield.vsm.inventory.dto.VnicDto>
  <objectId>500749e7-7d67-9f1b-3061-6f8740459094.000</objectId>
  <vnicUuid>500749e7-7d67-9f1b-3061-6f8740459094.000</vnicUuid>
  <portgroupId>virtualwire-2</portgroupId>
</com.vmware.vshield.vsm.inventory.dto.VnicDto>
'''


# deletePort test case configuration
NSX_PORT_DELETE_REQ_BODY = '''
<com.vmware.vshield.vsm.inventory.dto.VnicDto>
  <objectId>500749e7-7d67-9f1b-3061-6f8740459094.000</objectId>
  <vnicUuid>500749e7-7d67-9f1b-3061-6f8740459094.000</vnicUuid>
  <portgroupId></portgroupId>
</com.vmware.vshield.vsm.inventory.dto.VnicDto>
'''
