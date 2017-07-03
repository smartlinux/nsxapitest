#!/usr/bin/python
#
# SecurityGroup function test configration of NSX & vSphere environment.
#

# getSecurityGroup test case configuration
NSX_SECURITYGROUP_GET_ID = 'securitygroup-10'
NSX_SECURITYGROUP_UDPATE_ID = 'securitygroup-10'
NSX_SECURITYGROUP_DELETE_ID ='securitygroup-11'

# createSecurityGroup test case configuration

NSX_SECURITYGROUP_CREATE_REQ_BODY = '''
    <securitygroup>
    
        <objectTypeName>SecurityGroup</objectTypeName>
        <vsmUuid>42159F7C-2D59-F037-6676-C58C280182DC</vsmUuid>
        <nodeId>2fd5be66-5d1e-421c-b187-ffda32016534</nodeId>
        <revision>2</revision>
        <type>
            <typeName>SecurityGroup</typeName>
        </type>
        <name>Newgroup</name>
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
    </securitygroup>
'''


# updateSecurityGroup test case configuration

NSX_SECURITYGROUP_UPDATE_REQ_BODY = '''
    <securitygroup>
        <objectId>securitygroup-10</objectId>
        <objectTypeName>SecurityGroup</objectTypeName>
        <vsmUuid>42159F7C-2D59-F037-6676-C58C280182DC</vsmUuid>
        <nodeId>2fd5be66-5d1e-421c-b187-ffda32016534</nodeId>
        <revision>2</revision>
        <type>
            <typeName>SecurityGroup</typeName>
        </type>
        <name>Newgroup_update</name>
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
    </securitygroup>
'''


