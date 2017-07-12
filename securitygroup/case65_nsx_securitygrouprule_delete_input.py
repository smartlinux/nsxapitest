#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# SecurityGroup function test configration of NSX & vSphere environment.
#

NSX_SECURITYGROUP_ID = 'policy-5'

# updateSecurityGroup test case configuration


# revison后面的数字可能需要根据实际情况修改，只能大于等于原来的版本号

NSX_SECURITYGROUP_UPDATE_REQ_BODY = '''
<?xml version="1.0" encoding="UTF-8"?>
<securityPolicy>
    <objectId>policy-5</objectId>
    <objectTypeName>Policy</objectTypeName>

    <revision>26</revision>
    <type>
        <typeName>Policy</typeName>
    </type>
    <name>SP1</name>
    <description></description>
    <scope>
        <id>globalroot-0</id>
        <objectTypeName>GlobalRoot</objectTypeName>
        <name>Global</name>
    </scope>
    <clientHandle></clientHandle>
    <extendedAttributes/>
    <isUniversal>false</isUniversal>
    <universalRevision>0</universalRevision>
    <inheritanceAllowed>false</inheritanceAllowed>
    <precedence>4300</precedence>
    <actionsByCategory>
        <category>firewall</category>
        <action class="firewallSecurityAction">
            <objectId>firewallpolicyaction-1</objectId>
            <objectTypeName>FirewallPolicyAction</objectTypeName>
            <vsmUuid>42159F7C-2D59-F037-6676-C58C280182DC</vsmUuid>
            <nodeId>2fd5be66-5d1e-421c-b187-ffda32016534</nodeId>
            <revision>4</revision>
            <type>
                <typeName>FirewallPolicyAction</typeName>
            </type>
            <name>Rule1</name>
            <scope>
                <id>globalroot-0</id>
                <objectTypeName>GlobalRoot</objectTypeName>
                <name>Global</name>
            </scope>
            <clientHandle></clientHandle>
            <extendedAttributes/>
            <isUniversal>false</isUniversal>
            <universalRevision>0</universalRevision>
            <category>firewall</category>
            <executionOrder>1</executionOrder>
            <isEnabled>true</isEnabled>
            <isActionEnforced>false</isActionEnforced>
            <invalidSecondaryContainers>false</invalidSecondaryContainers>
            <invalidApplications>false</invalidApplications>
            <logged>false</logged>
            <action>allow</action>
            <direction>inbound</direction>
            <outsideSecondaryContainer>false</outsideSecondaryContainer>
        </action>
 

    </actionsByCategory>
    <statusesByCategory>
        <category>firewall</category>
        <status>in_sync</status>
    </statusesByCategory>
</securityPolicy>
'''


