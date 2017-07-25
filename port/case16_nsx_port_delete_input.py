#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Port function test configration of NSX & vSphere environment.
# 所谓删除Port操作，在nsx中就是将某VM从logical switch断开，从而去激活端口

# 在 venter mob 界面查找出 vm instanceUuid和网卡deviceId
# objectId/vnicUuid: Use these two values to form them. For example, if the VM instanceUuid is
# 502e71fa-1a00-759b-e40f-ce778e915f16 and the appropriate device value is device[4000], the objectId and
# vnicUuid are both 502e71fa-1a00-759b-e40f-ce778e915f16.000.
#
# portgroupId置空即可
NSX_PORT_DELETE_REQ_BODY = '''
<com.vmware.vshield.vsm.inventory.dto.VnicDto>
  <objectId>500749e7-7d67-9f1b-3061-6f8740459094.000</objectId>
  <vnicUuid>500749e7-7d67-9f1b-3061-6f8740459094.000</vnicUuid>
  <portgroupId></portgroupId>
</com.vmware.vshield.vsm.inventory.dto.VnicDto>
'''
