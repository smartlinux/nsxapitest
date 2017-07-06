#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# SecurityGroup function test configration of NSX & vSphere environment.
#

NSX_SECURITYGROUP_UDPATE_ID = 'securitygroup-10'

# updateSecurityGroup test case configuration


# revison后面的数字可能需要根据实际情况修改，只能大于等于原来的版本号

NSX_SECURITYGROUP_UPDATE_REQ_BODY = '''
    <securitygroup>
        <objectId>securitygroup-10</objectId>
        <objectTypeName>SecurityGroup</objectTypeName>


        <revision>3</revision>                            
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


