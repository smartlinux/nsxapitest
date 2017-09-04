#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test script for firewall function.
# 


import sys
import datetime
import libxml2
from io import StringIO

sys.path.append("..")
import rest

from nsx_basic_input import *

# PAY ATTENTION 
#need to get this ID and NAME before run this program
SECTIONID = "1014"  
SECTIONNAME = "TEST"


NSX_FIREWALL_RULE_CREATE_DATA_O = '''
            <rule  disabled="false" logged="false">
                <name>{s_ruleid}</name>
                <action>{s_action}</action>
                <appliedToList>
                    <appliedTo>
                        <name>DISTRIBUTED_FIREWALL</name>
                        <value>DISTRIBUTED_FIREWALL</value>
                        <type>DISTRIBUTED_FIREWALL</type>
                        <isValid>true</isValid>
                    </appliedTo>
                </appliedToList>
                
                <sources excluded="false">
                    <source>
                        <value>{s_sourceip}</value>
                        <type>Ipv4Address</type>
                        <isValid>true</isValid>
                    </source>
                </sources>
                <destinations excluded="false">
                    <destination>
                        <value>{s_dstip}</value>
                        <type>Ipv4Address</type>
                        <isValid>true</isValid>
                    </destination>
                </destinations>
                <services>
                    <service>
                        <isValid>true</isValid>
                        <destinationPort>{s_dstport}</destinationPort>
                        <protocol>6</protocol>
                        <protocolName>TCP</protocolName>
                    </service>
                </services>
                <direction>inout</direction>
                <packetType>any</packetType>
            </rule>

'''


restclient = rest.Rest(NSX_IP, NSX_USER, NSX_PWD, True)



payload ='<section id="'+SECTIONID+'" name="'+SECTIONNAME+'" type="LAYER3">'


def createpayloadtest():

    base=0
    for num in range(1,255):
        if (num %2)==0:
            action='deny'
        else:
            action="allow"
        source='20.0.0.'+str(num)
        dest='21.0.0.'+str(num)
        port=str(1000+num)
        ruleid="test rule id "+str(base+num)
        createpayloadOne(ruleid,action,source,dest,port)

   
def createpayload():

    base=0
    for num in range(1,255):
        if (num %2)==0:
            action='deny'
        else:
            action="allow"
        source='20.0.0.'+str(num)
        dest='21.0.0.'+str(num)
        port=str(1000+num)
        ruleid="test rule id "+str(base+num)
        createpayloadOne(ruleid,action,source,dest,port)

    base=base+254


 
    for num in range(1,255):
        if (num %2)==0:
            action='deny'
        else:
            action="allow"
        source='20.0.1.'+str(num)
        dest='21.0.1.'+str(num)
        port=str(2000+num)
        ruleid="test rule id "+str(base+num)
        createpayloadOne(ruleid,action,source,dest,port)

    base=base+254

    for num in range(1,255):
        if (num %2)==0:
            action='deny'
        else:
            action="allow"
        source='20.0.2.'+str(num)
        dest='21.0.2.'+str(num)
        port=str(3000+num)
        ruleid="test rule id "+str(base+num)
        createpayloadOne(ruleid,action,source,dest,port)

    base=base+254
    for num in range(1,239):
        if (num %2)==0:
            action='deny'
        else:
            action="allow"
        source='20.0.3.'+str(num)
        dest='21.0.3.'+str(num)
        port=str(4000+num)
        ruleid="test rule id "+str(base+num)
        createpayloadOne(ruleid,action,source,dest,port)





def createpayloadOne(ruleid,action,source,dest,port):
    global payload
    NSX_FIREWALL_RULE_CREATE_DATA = NSX_FIREWALL_RULE_CREATE_DATA_O.format(s_ruleid=ruleid,s_action=action,s_sourceip=source,s_dstip=dest,s_dstport=port)
    payload=payload +  NSX_FIREWALL_RULE_CREATE_DATA 

def addFirewallRule():
    global payload

    createpayload()
    payload=payload+'</section>'
    print payload

    respData = restclient.get(NSX_URL+'/api/4.0/firewall/globalroot-0/config/layer3sections/'+SECTIONID, 'getFirewallSection')

    debuginfo=restclient.getDebugInfo()
    strio =StringIO()
    strio.write(unicode(debuginfo))
    xetag = str(restclient.getHTTPHeader(strio,"ETag"))
    etag=xetag.strip()

    NSX_FIREWALL_POLICY_ETAG = etag
    print  "etag",NSX_FIREWALL_POLICY_ETAG
    
    moreHeaders = ['If-Match: '+NSX_FIREWALL_POLICY_ETAG ]
   
    URL_O='{S_NSXURL}/api/4.0/firewall/globalroot-0/config/layer3sections/{S_SECTIONID}'
    URL = URL_O.format(S_NSXURL=NSX_URL,S_SECTIONID=SECTIONID)
  
    respData = restclient.put(URL, payload, 'createFirewallRule1000', moreHeaders)
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
