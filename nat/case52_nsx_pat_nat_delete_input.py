#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# NAT function test configration of NSX & vSphere environment.
# PAT NAT: 同时用address和port来映射

# NSX Edge ID, 可在web client-> NSX Edges界面找到
NSX_EDGE_ID = 'edge-9'

# 要删除的floatingIP所对应的nat ruleID
NSX_NAT_RULE_ID = '196614'