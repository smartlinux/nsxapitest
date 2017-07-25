#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# QOS function test configration of NSX & vSphere environment.
#

# QOS所在的Edge ID（不能是DLR），可以在web client-> NSX edges里找到
NSX_EDGE_ID = 'edge-9'

# Edge Interface Index，可以在web client-> NSX edges->Manage->Settings->Interface->vNIC#里找到
NSX_EDGE_INTERFACE_INDEX = '0'

inShapingPolicy_averageBandwidth = '50000'
inShapingPolicy_peakBandwidth = '400000'
inShapingPolicy_enabled = 'true'

outShapingPolicy_averageBandwidth = '40000'
outShapingPolicy_peakBandwidth = '300000'
outShapingPolicy_enabled = 'true'
