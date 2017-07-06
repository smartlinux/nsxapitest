#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# SecurityGroup function test configration of NSX & vSphere environment.
#



# createSecurityGroup test case configuration

NSX_SECURITYGROUP_CREATE_REQ_BODY = '''
    <securitygroup>
    
        <objectTypeName>SecurityGroup</objectTypeName>

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
