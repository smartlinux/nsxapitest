#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# FloatingIP function test configration of NSX & vSphere environment.
#

# NSX Edge ID, 可在web client-> NSX Edges界面找到
NSX_EDGE_ID = 'edge-7'

# 要删除的floatingIP所对应的nat ruleID
NSX_NAT_RULE_ID_LIST = ['196613', '196614']