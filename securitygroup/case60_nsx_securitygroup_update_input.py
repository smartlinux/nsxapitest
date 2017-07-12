#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# SecurityGroup function test configration of NSX & vSphere environment.
#

NSX_SECURITYGROUP_UDPATE_ID = 'policy-9'

# updateSecurityGroup test case configuration


# revison后面的数字可能需要根据实际情况修改，只能大于等于原来的版本号

NSX_SECURITYGROUP_UPDATE_REQ_BODY = '''
<securityPolicy>
    <objectId>policy-9</objectId>
    <objectTypeName>Policy</objectTypeName>

    <revision>6</revision>
    <type>
        <typeName>Policy</typeName>
    </type>
    <name>SP10001</name>
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
    <precedence>4500</precedence>
    <statusesByCategory>
        <category>firewall</category>
        <status>in_sync</status>
    </statusesByCategory>
    <statusesByCategory>
        <category>traffic_steering</category>
        <status>in_sync</status>
    </statusesByCategory>
</securityPolicy>
'''


