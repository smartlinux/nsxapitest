#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for edge firewall function.
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
EDGEID="edge-1"


NSX_FIREWALL_RULE_CREATE_DATA_O = '''
        <firewallRule>
            <name>{s_rulename}</name>
            <enabled>true</enabled>
            <loggingEnabled>false</loggingEnabled>
            <description></description>
            <matchTranslated>false</matchTranslated>
            <action>{s_action}</action>
            <source>
                <exclude>false</exclude>
                <ipAddress>{s_sourceip}</ipAddress>
            </source>
            <destination>
                <exclude>false</exclude>
                <ipAddress>{s_dstip}</ipAddress>
            </destination>
            <application>
                <service>
                    <protocol>tcp</protocol>
                    <port>{s_dstport}</port>
                    <sourcePort>any</sourcePort>
                </service>
            </application>
        </firewallRule>
'''


restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)



payload ='<firewallRules> '
base=0

def createpayloadtest():

    localbase=0
    for num in range(1,255):
        if (num %2)==0:
            action='deny'
        else:
            action="accept"
        source='20.0.0.'+str(num)
        dest='21.0.0.'+str(num)
        port=str(1000+num)
        rulename="test rule id "+str(localbase+num)
        createpayloadOne(rulename,action,source,dest,port)

   
def createpayload1():

    global base
    for num in range(1,255):
        if (num %2)==0:
            action='deny'
        else:
            action="accept"
        source='20.0.0.'+str(num)
        dest='21.0.0.'+str(num)
        port=str(1000+num)
        rulename="test rule id "+str(base+num)
        createpayloadOne(rulename,action,source,dest,port)

    base=base+254

def createpayload2():
    global base 
    for num in range(1,255):
        if (num %2)==0:
            action='deny'
        else:
            action="accept"
        source='20.0.1.'+str(num)
        dest='21.0.1.'+str(num)
        port=str(2000+num)
        rulename="test rule id "+str(base+num)
        createpayloadOne(rulename,action,source,dest,port)

    base=base+254

def createpayload3():
    global base
    for num in range(1,255):
        if (num %2)==0:
            action='deny'
        else:
            action="accept"
        source='20.0.2.'+str(num)
        dest='21.0.2.'+str(num)
        port=str(3000+num)
        rulename="test rule id "+str(base+num)
        createpayloadOne(rulename,action,source,dest,port)

    base=base+254

def createpayload4():
    global base
    for num in range(1,239):
        if (num %2)==0:
            action='deny'
        else:
            action="accept"
        source='20.0.3.'+str(num)
        dest='21.0.3.'+str(num)
        port=str(4000+num)
        rulename="test rule id "+str(base+num)
        createpayloadOne(rulename,action,source,dest,port)





def createpayloadOne(rulename,action,source,dest,port):
    global payload
    NSX_FIREWALL_RULE_CREATE_DATA = NSX_FIREWALL_RULE_CREATE_DATA_O.format(s_rulename=rulename,s_action=action,s_sourceip=source,s_dstip=dest,s_dstport=port)
    payload=payload +  NSX_FIREWALL_RULE_CREATE_DATA 

def addFirewallRule():
    global payload

    URL_O='{S_NSXURL}/api/4.0/edges/{S_EDGEID}/firewall/config/rules'
    URL = URL_O.format(S_NSXURL=NSX_URL,S_EDGEID=EDGEID)
    print URL

    payload ='<firewallRules> '
    createpayload1()
    payload=payload+'  </firewallRules>'
     
    respData = restclient.post(URL, payload, 'createEdgeFirewallRule1000')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))    



    payload ='<firewallRules> '
    createpayload2()
    payload=payload+'  </firewallRules>'
     
    respData = restclient.post(URL, payload, 'createEdgeFirewallRule1000')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))    


    payload ='<firewallRules> '
    createpayload3()
    payload=payload+'  </firewallRules>'
     
    respData = restclient.post(URL, payload, 'createEdgeFirewallRule1000')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))    


    payload ='<firewallRules> '
    createpayload4()
    payload=payload+'  </firewallRules>'
     
    respData = restclient.post(URL, payload, 'createEdgeFirewallRule1000')
    output(restclient.getDebugInfo() + restclient.prettyPrint(respData))    



def output(msg):
    f = file(datetime.datetime.now().strftime("../log/" +  "_output_20%y%m%d%H%M%S.log"), "w")
    f.write(msg)
    f.close()	


def main():
    addFirewallRule()
    print "NSX API",  "completed successfully!"

if __name__ == "__main__":
    sys.exit(main())
