#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Port function test configration of NSX & vSphere environment.
#

# 要获取的端口ID，由网络ID和portKey组成，portKey在web client->dvSwitch->portgroup->manage->ports里面找到
NSX_PORT_ID = 'virtualwire-2.35'

# 查询的开始时间和结束时间，格式必须正确
QUERY_START_TIME = "2017-08-31 12:10:00"
QUERY_END_TIME = "2017-03-04 12:20:30"
