#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Port function test configration of NSX & vSphere environment.
#


# objectId/vnicUuid: Use these two values to form them. For example, if the VM instanceUuid is
# 502e71fa-1a00-759b-e40f-ce778e915f16 and the appropriate device value is device[4000], the objectId and
# vnicUuid are both 502e71fa-1a00-759b-e40f-ce778e915f16.000.
#
# portgroupId: 要创建端口所在的网络ID，该ID可以在network_list的执行结果中找到，或者在web client->logical switch->Summary界面找到
NSX_PORT_CREATE_REQ_BODY = '''
<com.vmware.vshield.vsm.inventory.dto.VnicDto>
  <objectId>500749e7-7d67-9f1b-3061-6f8740459094.000</objectId>
  <vnicUuid>500749e7-7d67-9f1b-3061-6f8740459094.000</vnicUuid>
  <portgroupId>virtualwire-2</portgroupId>
</com.vmware.vshield.vsm.inventory.dto.VnicDto>
'''
