#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Port function test configration of NSX & vSphere environment.
# 修改端口的mac address和qos shaping policy


# 要获取的端口ID，由网络ID和portKey组成，portKey在web client->dvSwitch->portgroup->manage->ports里面找到
NSX_PORT_ID = 'virtualwire-2.35'

NEW_MAC_ADDRESS = '00:50:56:bb:4b:45'

IN_SHAPING_ENABLE = 'true'
IN_SHAPING_AVERAGE_BPS = 14000000
IN_SHAPING_PEAK_BPS = 24000000

OUT_SHAPING_ENABLE = 'true'
OUT_SHAPING_AVERAGE_BPS = 15000000
OUT_SHAPING_PEAK_BPS = 25000000

