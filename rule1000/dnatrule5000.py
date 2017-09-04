#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script create 5000 edge dnat rules.
# 


import sys
import datetime
import libxml2
from io import StringIO

sys.path.append("..")
import rest

from nsx_basic_input import *

# PAY ATTENTION 
#need to get this ID 
EDGE_ID = "edge-1"

# vnic should be the uplink vnic
NSX_DNAT_RULE_CREATE_DATA_O = '''
  <natRule>
    <action>dnat</action>
    <vnic>0</vnic>
    <originalAddress>{orig_addr}</originalAddress>
    <translatedAddress>{tran_addr}</translatedAddress>
    <loggingEnabled>false</loggingEnabled>
    <enabled>true</enabled>
    <description>{rule_desc}</description>
    <protocol>any</protocol>
    <translatedPort>any</translatedPort>
    <originalPort>any</originalPort>
  </natRule>
'''


restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)

payload = '<natRules> '
base = 0

def createpayloadOne(origAddr, tranAddr, ruleDesc):
    global payload
    NSX_DNAT_RULE_CREATE_DATA = NSX_DNAT_RULE_CREATE_DATA_O.format(orig_addr=origAddr,tran_addr=tranAddr,rule_desc=ruleDesc)
    payload = payload +  NSX_DNAT_RULE_CREATE_DATA 

	
def createpayload250(subnetId):
    global base
    for num in range(1,250):
	    base = base + 1
        origAddr = '2.1.%d.%d'%(subnetId, num)
        tranAddr = '20.1.%d.%d'%(subnetId, num)
        ruleDesc="test rule id %d"%(base)
        createpayloadOne(origAddr, tranAddr, ruleDesc)

		
def createDnatRule5000():
    global payload

    URL = '%s/api/4.0/edges/%s/nat/config/rules'%(NSX_URL,EDGE_ID)
    print URL

    for subnetid in range(2,21):
        print 'Try to create DNAT from origAddr 2.1.%d.x to tranAddr 20.1.%d.x'%(subnetid)
        payload ='<natRules>'
        createpayload250(subnetid)
        payload = payload + '</natRules>'
        respData = restclient.post(URL, payload, 'createDnat250')
        print 'DNAT from origAddr 2.1.%d.x to tranAddr 20.1.%d.x created.'%(subnetid)


def main():
    createDnatRule5000()
    print "Invoke NSX API to create 5000 dnat rules completed successfully!"

if __name__ == "__main__":
    sys.exit(main())
