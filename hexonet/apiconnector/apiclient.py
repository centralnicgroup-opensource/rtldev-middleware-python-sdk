# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector.apiclient
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all necessary functionality for http communicatiton
    with our Backend System.
    :copyright: © 2018 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""

from hexonet.apiconnector.response import Response
from hexonet.apiconnector.responsetemplatemanager import ResponseTemplateManager as RTM
from hexonet.apiconnector.socketconfig import SocketConfig
from urllib.parse import quote, unquote, urlparse, urlencode
from urllib.request import urlopen, Request
import re
import copy
import platform

rtm = RTM()


class APIClient(object):

    def __init__(self):
        # API connection url
        self.setURL("https://api.ispapi.net/api/call.cgi")
        # Object covering API connection data
        self.__socketConfig = SocketConfig()
        # activity flag for debug mode
        self.__debugMode = False
        # API connection timeout setting
        self.__socketTimeout = 300000
        self.useLIVESystem()
        # user agent setting
        self.__ua = ""

    def enableDebugMode(self):
        """
        Enable Debug Output to STDOUT
        """
        self.__debugMode = True
        return self

    def disableDebugMode(self):
        """
        Disable Debug Output
        """
        self.__debugMode = False
        return self

    def getPOSTData(self, cmd):
        """
        Serialize given command for POST request including connection configuration data
        """
        data = self.__socketConfig.getPOSTData()
        tmp = ""
        if not isinstance(cmd, str):
            for key in sorted(cmd.keys()):
                if (cmd[key] is not None):
                    tmp += ("{0}={1}\n").format(key, re.sub('[\r\n]', '', str(cmd[key])))
        return ("{0}{1}={2}").format(data, quote('s_command'), quote(re.sub('\n$', '', tmp)))

    def getSession(self):
        """
        Get the API Session that is currently set
        """
        return self.__socketConfig.getSession()

    def getURL(self):
        """
        Get the API connection url that is currently set
        """
        return self.__socketURL

    def getUserAgent(self):
        """
        Get the User Agent
        """
        if (len(self.__ua) == 0):
            pid = "PYTHON-SDK"
            pyv = platform.python_version()
            pf = platform.system()
            arch = platform.architecture()[0]
            self.__ua = "%s (%s; %s; rv:%s) python/%s" % (pid, pf, arch, self.getVersion(), pyv)
        return self.__ua

    def setUserAgent(self, pid, rv):
        """
        Possibility to customize default user agent to fit your needs by given string and revision
        """
        pyv = platform.python_version()
        pf = platform.system()
        arch = platform.architecture()[0]
        self.__ua = "%s (%s; %s; rv:%s) python-sdk/%s python/%s" % (pid, pf, arch, rv, self.getVersion(), pyv)
        return self

    def getVersion(self):
        """
        Get the current module version
        """
        return "3.1.1"

    def saveSession(self, session):
        """
        Apply session data (session id and system entity) to given client request session
        """
        session["socketcfg"] = {
            "entity": self.__socketConfig.getSystemEntity(),
            "session": self.__socketConfig.getSession()
        }
        return self

    def reuseSession(self, session):
        """
        Use existing configuration out of session
        to rebuild and reuse connection settings
        """
        self.__socketConfig.setSystemEntity(session["socketcfg"]["entity"])
        self.setSession(session["socketcfg"]["session"])
        return self

    def setURL(self, value):
        """
        Set another connection url to be used for API communication
        """
        self.__socketURL = value
        return self

    def setOTP(self, value):
        """
        Set one time password to be used for API communication
        """
        self.__socketConfig.setOTP(value)
        return self

    def setSession(self, value):
        """
        Set an API session id to be used for API communication
        """
        self.__socketConfig.setSession(value)
        return self

    def setRemoteIPAddress(self, value):
        """
        Set an Remote IP Address to be used for API communication.
        To be used in case you have an active ip filter setting.
        """
        self.__socketConfig.setRemoteAddress(value)
        return self

    def setCredentials(self, uid, pw):
        """
        Set Credentials to be used for API communication
        """
        self.__socketConfig.setLogin(uid)
        self.__socketConfig.setPassword(pw)
        return self

    def setRoleCredentials(self, uid, role, pw):
        """
        Set Credentials to be used for API communication
        """
        if (role == ''):
            return self.setCredentials(uid, pw)
        return self.setCredentials(("{0}!{1}").format(uid, role), pw)

    def login(self, otp=""):
        """
        Perform API login to start session-based communication
        """
        self.setOTP(otp)
        rr = self.request({"COMMAND": "StartSession"})
        if (rr.isSuccess()):
            col = rr.getColumn("SESSION")
            self.setSession(col.getData()[0] if (col is not None) else None)
        return rr

    def loginExtended(self, params, otp=""):
        """
        Perform API login to start session-based communication.
        Use given specific command parameters.
        """
        self.setOTP(otp)
        cmd = {
            "COMMAND": "StartSession"
        }
        cmd.update(params)
        rr = self.request(cmd)
        if (rr.isSuccess()):
            col = rr.getColumn("SESSION")
            self.setSession(col.getData()[0] if (col is not None) else None)
        return rr

    def logout(self):
        """
        Perform API logout to close API session in use
        """
        rr = self.request({
            "COMMAND": "EndSession",
        })
        if (rr.isSuccess()):
            self.setSession(None)
        return rr

    def request(self, cmd):
        """
        Perform API request using the given command
        """
        data = self.getPOSTData(cmd).encode('UTF-8')
        # TODO: 300s (to be sure to get an API response)
        try:
            req = Request(self.__socketURL, data, {
                'User-Agent': self.getUserAgent()
            })
            body = urlopen(req, timeout=self.__socketTimeout).read()
            if (self.__debugMode):
                print((self.__socketURL, data, body, '\n', '\n'))
        except Exception:
            body = rtm.getTemplate("httperror").getPlain()
            if (self.__debugMode):
                print((self.__socketURL, data, "HTTP communication failed", body, '\n', '\n'))
        return Response(body, cmd)

    def requestNextResponsePage(self, rr):
        """
        Request the next page of list entries for the current list query
        Useful for tables
        """
        mycmd = self.__toUpperCaseKeys(rr.getCommand())
        if ("LAST" in mycmd):
            raise Exception("Parameter LAST in use. Please remove it to avoid issues in requestNextPage.")
        first = 0
        if ("FIRST" in mycmd):
            first = mycmd["FIRST"]
        total = rr.getRecordsTotalCount()
        limit = rr.getRecordsLimitation()
        first += limit
        if (first < total):
            mycmd["FIRST"] = first
            mycmd["LIMIT"] = limit
            return self.request(mycmd)
        else:
            return None

    def requestAllResponsePages(self, cmd):
        """
        Request all pages/entries for the given query command
        """
        responses = []
        mycmd = copy.deepcopy(cmd)
        mycmd["FIRST"] = 0
        rr = self.request(mycmd)
        tmp = rr
        while tmp is not None:
            responses.append(tmp)
            tmp = self.requestNextResponsePage(tmp)
            if tmp is None:
                break
        return responses

    def setUserView(self, uid):
        """
        Set a data view to a given subuser
        """
        self.__socketConfig.setUser(uid)
        return self

    def resetUserView(self):
        """
        Reset data view back from subuser to user
        """
        self.__socketConfig.setUser(None)
        return self

    def useOTESystem(self):
        """
        Set OT&E System for API communication
        """
        self.__socketConfig.setSystemEntity("1234")
        return self

    def useLIVESystem(self):
        """
        Set LIVE System for API communication (this is the default setting)
        """
        self.__socketConfig.setSystemEntity("54cd")
        return self

    def __toUpperCaseKeys(self, cmd):
        """
        Translate all command parameter names to uppercase
        """
        newcmd = {}
        for k in list(cmd.keys()):
            newcmd[k.upper()] = cmd[k]
        return newcmd
