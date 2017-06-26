#!/usr/bin/python
#
# PROGRAM REQUIREMENTS: This program requires python 2.5 or later to
# run. This program also requires the pycurl package to be
# installed. It is not normally installed by default, but most Linux
# distributions have the packages available. Otherwise, you can
# download it from:
#
# pycurl          http://pycurl.sourceforge.net/
#
# rest.py
#
# This code implements a rest interface.
#

import sys
import pycurl
import libxml2
import StringIO
import subprocess
import re

class RestException(Exception):
    pass

class Rest:
    """REST API"""
    # ------------------------------------------------------------------------
    #
    # REST API Interfaces
    #
    # ------------------------------------------------------------------------

    def __init__(self, host, username, password, verbose = False):
        """__init__(host, username, password, verbose = False)"""
        self.host = host
        self.username = username
        self.password = password
        self.verbose = verbose
        self.debuginfo = ''


    #
    # Allocate a new Curl object with some defaults
    #
    def newCurl(self, url, moreHeaders=None):
        """newCurl(url, moreHeaders=None)"""
        cobj = pycurl.Curl()
        cobj.setopt(pycurl.URL, str(url))
        cobj.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
        cobj.setopt(pycurl.USERPWD, self.username + ":" + self.password)
        cobj.setopt(pycurl.HTTPHEADER, self.sendHeaders(more = moreHeaders))
        cobj.setopt(pycurl.SSL_VERIFYPEER, 0)
        cobj.setopt(pycurl.SSL_VERIFYHOST, 0)
        cobj.setopt(pycurl.FOLLOWLOCATION, 1)
        cobj.setopt(pycurl.FAILONERROR, 0)
        cobj.setopt(pycurl.PROXY, "")
        if self.verbose:
            cobj.setopt(pycurl.VERBOSE, 1)
            cobj.setopt(pycurl.DEBUGFUNCTION, self.debug)
            self.debuginfo = ''
        return cobj


    #
    # Allocate a curl object for POST
    #
    def newCurlPost(self, url, request, moreHeaders=None):
        """newCurlPost(url, request, moreHeaders=None)"""
        cobj = self.newCurl(url)
        cobj.setopt(pycurl.URL, str(url))
        cobj.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
        cobj.setopt(pycurl.USERPWD, self.username + ":" + self.password)
        cobj.setopt(pycurl.HTTPHEADER, self.sendHeaders(more = moreHeaders))
        cobj.setopt(pycurl.POST, 1)
        cobj.setopt(pycurl.POSTFIELDS, request)
        cobj.setopt(pycurl.POSTFIELDSIZE, len(request))
        if self.verbose:
            cobj.setopt(pycurl.VERBOSE, 1)
        return cobj


    #
    # Allocate a curl object for PUT
    #
    def newCurlPut(self, url, moreHeaders=None):
        """newCurlPut(url, moreHeaders=None)"""
        cobj = self.newCurl(url)
        cobj.setopt(pycurl.URL, str(url))
        cobj.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
        cobj.setopt(pycurl.USERPWD, self.username + ":" + self.password)
        cobj.setopt(pycurl.HTTPHEADER, self.sendHeaders(more = moreHeaders))
        cobj.setopt(pycurl.PUT, 1)
        cobj.setopt(pycurl.UPLOAD, 1)
        if self.verbose:
            cobj.setopt(pycurl.VERBOSE, 1)
        return cobj


    #
    # Return the proper headers for the nsx Management Plane REST API
    #
    def sendHeaders(self, more=None):
        """sendHeaders(more=None)"""
        headers = ["Accept: application/xml", "Content-type: application/xml"]
        if more:
            for header in more:
                headers.append(header)
        return headers


    #
    # Retrieve a specific header named 'which'
    # from 'buf' (which is a StringIO() object)
    #
    def getHTTPHeader(self, buf, which):
        """getHTTPHeader(buf, which)"""
        buf.seek(0)
        headers = buf.readlines()
        for header in headers:
            hv = header.split(':', 1)
            if hv[0] == which:
                return hv[1]
        return None

    #
    # Return true if the passed http response code
    # is a successful one (somewhere in the 200s)
    #
    def isSuccessful(self, resp):
        """isSuccessful(resp)"""
        return resp >= 200 and resp < 300


    #
    # Extract out the error code and description
    # from a returned packet
    #
    def extractError(self, ret):
        """extractError(ret)"""
        errorCode = ""
        errorDescription = ""
        try:
            doc = libxml2.parseDoc(ret)
            xp = doc.xpathNewContext()

            node = xp.xpathEval("//error/errorCode")
            if len(node):
                errorCode = node[0].content

            node = xp.xpathEval("//error/details")
            if len(node):
                errorDescription = node[0].content

            doc.freeDoc()
        except:
            return ret
        return errorCode + ' ' + errorDescription



    #
    # Generic GET of the given url, returning the result
    #
    def get(self, url, caller):
        """get(url, caller)"""
        ret = ''
        buf = StringIO.StringIO()
        cobj = self.newCurl(url)
        cobj.setopt(pycurl.WRITEFUNCTION, buf.write)
        try:
            cobj.perform()
        except Exception, msg:
            ret = buf.getvalue()
            raise RestException, caller + ":" + str(msg) + ":" + ret
        finally:
            ret = buf.getvalue()
            if not self.isSuccessful(cobj.getinfo(pycurl.RESPONSE_CODE)):
                raise RestException, caller + ": " + self.extractError(ret)
            cobj.close()
            buf.close()
        return ret


    #
    # generic POST to the give url using the request
    # provided, returning the result
    #
    def post(self, url, request, caller):
        """post(url, request, caller)"""
        if self.verbose and len(request):
            print >> sys.stderr, "POST REQUEST:"
            print >> sys.stderr, self.prettyPrint(request)
        ret = ''
        buf = StringIO.StringIO()
        cobj = self.newCurlPost(url, request)
        cobj.setopt(pycurl.WRITEFUNCTION, buf.write)
        try:
            cobj.perform()
        except Exception, msg:
            ret = buf.getvalue()
            raise RestException, caller + ":" + str(msg) + ":" + ret
        finally:
            ret = buf.getvalue()
            if not self.isSuccessful(cobj.getinfo(pycurl.RESPONSE_CODE)):
                raise RestException, caller + ": " + self.extractError(ret)
            cobj.close()
            buf.close()
        return ret


    #
    # generic PUT to the give url using the request
    # provided, returning the result
    #
    def put(self, url, request, caller):
        """put(url, request, caller)"""
        if self.verbose and len(request):
            print >> sys.stderr, "PUT REQUEST:"
            print >> sys.stderr, self.prettyPrint(request)
        ret = ''
        buf = StringIO.StringIO()
        putbuf = StringIO.StringIO()
        putbuf.write(request)
        putbuf.seek(0)

        cobj = self.newCurlPut(url)
        cobj.setopt(pycurl.WRITEFUNCTION, buf.write)
        cobj.setopt(pycurl.READFUNCTION, putbuf.read)
        try:
            cobj.perform()
        except Exception, msg:
            ret = buf.getvalue()
            raise RestException, caller + ":" + str(msg) + ":" + ret
        finally:
            ret = buf.getvalue()
            if not self.isSuccessful(cobj.getinfo(pycurl.RESPONSE_CODE)):
                raise RestException, caller + ": " + self.extractError(ret)
            cobj.close()
            putbuf.close()
            buf.close()

        return ret



    #
    # Invoke an http DELETE on the given url,
    # returning the result
    #
    def delete(self, url, caller):
        """delete(url, caller)"""
        ret = ''
        buf = StringIO.StringIO()
        cobj = self.newCurl(url)
        cobj.setopt(pycurl.WRITEFUNCTION, buf.write)
        cobj.setopt(pycurl.CUSTOMREQUEST, "DELETE")
        try:
            cobj.perform()
        except Exception, msg:
            ret = buf.getvalue()
            raise RestException, caller + ":" + str(msg) + ":" + ret
        finally:
            ret = buf.getvalue()
            if not self.isSuccessful(cobj.getinfo(pycurl.RESPONSE_CODE)):
                raise RestException, caller + ": " + self.extractError(ret)
            cobj.close()
            buf.close()
        return ret



    #
    # format the given xml
    #
    def prettyPrint(self, xml):
        """prettyPrint(xml)"""
        try:
            doc = libxml2.parseDoc(xml)
            return doc.serialize('UTF-8', 1)
        except:
            return xml

    #
    # callback for pycurl debug information, only need to record type 1(HEADER_IN) and 2(HEADER_OUT) messages.
    #
    def debug(self, debug_type, debug_msg):
        if debug_type in [1,2]:
            self.debuginfo += debug_msg

    #
    # get current curl session's debug info, include HEADER_IN and HEADER_OUT info
    #
    def getDebugInfo(self):
        return self.debuginfo
