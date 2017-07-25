#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# QOS function test configration of NSX & vSphere environment.
#

# QOS所在的Edge ID（不能是DLR），可以在web client-> NSX edges里找到
NSX_EDGE_ID = 'edge-9'

# Edge Interface Index，可以在web client-> NSX edges->Manage->Settings->Interface->vNIC#里找到
NSX_EDGE_INTERFACE_INDEX = '0'

inShapingPolicy_averageBandwidth = '51200'
inShapingPolicy_peakBandwidth = '458000'
inShapingPolicy_enabled = 'true'

outShapingPolicy_averageBandwidth = '47900'
outShapingPolicy_peakBandwidth = '336000'
outShapingPolicy_enabled = 'false'
