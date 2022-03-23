# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector.apiclient
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all necessary functionality for http communicatiton
    with our Backend System.
    :copyright: © 2018 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""

from hexonet.apiconnector.logger import Logger
from hexonet.apiconnector.response import Response
from hexonet.apiconnector.responsetemplatemanager import ResponseTemplateManager as RTM
from hexonet.apiconnector.socketconfig import SocketConfig
from urllib.parse import quote, unquote, urlparse, urlencode
from urllib.request import urlopen, Request
import re
import copy
import platform

rtm = RTM()

ISPAPI_CONNECTION_URL_PROXY = "http://127.0.0.1/api/call.cgi"
ISPAPI_CONNECTION_URL_LIVE = "https://api.ispapi.net/api/call.cgi"
ISPAPI_CONNECTION_URL_OTE = "https://api-ote.ispapi.net/api/call.cgi"


class APIClient(object):
    def __init__(self):
        # API connection url
        self.setURL(ISPAPI_CONNECTION_URL_LIVE)
        # Object covering API connection data
        self.__socketConfig = SocketConfig()
        # activity flag for debug mode
        self.__debugMode = False
        # API connection timeout setting
        self.__socketTimeout = 300000
        self.useLIVESystem()
        # user agent setting
        self.__ua = ""
        # additional connection settings
        self.__curlopts = {}
        # logger class instance
        self.setDefaultLogger()

    def setCustomLogger(self, logger):
        """
        Set custom logger to use instead of the default one
        """
        self.__logger = logger
        return self

    def setDefaultLogger(self):
        """
        Set default logger to use
        """
        self.__logger = Logger()
        return self

    def setProxy(self, proxy):
        """
        Set Proxy to use for API communication
        """
        if proxy == "":
            self.__curlopts.pop("PROXY", None)
        else:
            self.__curlopts["PROXY"] = proxy
        return self

    def getProxy(self):
        """
        Get Proxy configuration value for API communication
        """
        if "PROXY" in self.__curlopts:
            return self.__curlopts["PROXY"]
        return None

    def setReferer(self, referer):
        """
        Set the Referer Header to use for API communication
        """
        if referer == "":
            self.__curlopts.pop("REFERER", None)
        else:
            self.__curlopts["REFERER"] = referer
        return self

    def getReferer(self):
        """
        Get the Referer Header configuration value
        """
        if "REFERER" in self.__curlopts:
            return self.__curlopts["REFERER"]
        return None

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

    def getPOSTData(self, cmd, secured=False):
        """
        Serialize given command for POST request including connection configuration data
        """
        data = self.__socketConfig.getPOSTData()
        if secured:
            data = re.sub(r"s_pw=[^&]+", "s_pw=***", data)
        tmp = ""
        if not isinstance(cmd, str):
            for key in sorted(cmd.keys()):
                if cmd[key] is not None:
                    tmp += ("{0}={1}\n").format(
                        key, re.sub("[\r\n]", "", str(cmd[key]))
                    )
        else:
            tmp = cmd
        tmp = tmp.rstrip("\n")
        if secured:
            tmp = re.sub(r"PASSWORD=[^\n]+", "PASSWORD=***", tmp)
        return ("{0}{1}={2}").format(
            data, quote("s_command"), quote(re.sub("\n$", "", tmp))
        )

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
        if len(self.__ua) == 0:
            pid = "PYTHON-SDK"
            pyv = platform.python_version()
            pf = platform.system()
            arch = platform.architecture()[0]
            self.__ua = "%s (%s; %s; rv:%s) python/%s" % (
                pid,
                pf,
                arch,
                self.getVersion(),
                pyv,
            )
        return self.__ua

    def setUserAgent(self, pid, rv, modules=[]):
        """
        Possibility to customize default user agent to fit your needs by given string and revision
        """
        s = " "
        mods = ""
        if len(modules) > 0:
            mods += " " + s.join(modules)
        pyv = platform.python_version()
        pf = platform.system()
        arch = platform.architecture()[0]
        self.__ua = "%s (%s; %s; rv:%s)%s python-sdk/%s python/%s" % (
            pid,
            pf,
            arch,
            rv,
            mods,
            self.getVersion(),
            pyv,
        )
        return self

    def getVersion(self):
        """
        Get the current module version
        """
        return "3.8.3"

    def saveSession(self, session):
        """
        Apply session data (session id and system entity) to given client request session
        """
        session["socketcfg"] = {
            "entity": self.__socketConfig.getSystemEntity(),
            "session": self.__socketConfig.getSession(),
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
        if role == "":
            return self.setCredentials(uid, pw)
        return self.setCredentials(("{0}!{1}").format(uid, role), pw)

    def login(self, otp=""):
        """
        Perform API login to start session-based communication
        """
        self.setOTP(otp)
        rr = self.request({"COMMAND": "StartSession"})
        if rr.isSuccess():
            col = rr.getColumn("SESSION")
            self.setSession(col.getData()[0] if (col is not None) else None)
        return rr

    def loginExtended(self, params, otp=""):
        """
        Perform API login to start session-based communication.
        Use given specific command parameters.
        """
        self.setOTP(otp)
        cmd = {"COMMAND": "StartSession"}
        cmd.update(params)
        rr = self.request(cmd)
        if rr.isSuccess():
            col = rr.getColumn("SESSION")
            self.setSession(col.getData()[0] if (col is not None) else None)
        return rr

    def logout(self):
        """
        Perform API logout to close API session in use
        """
        rr = self.request(
            {
                "COMMAND": "EndSession",
            }
        )
        if rr.isSuccess():
            self.setSession(None)
        return rr

    def request(self, cmd):
        """
        Perform API request using the given command
        """
        # flatten nested api command bulk parameters
        newcmd = self.__flattenCommand(cmd)
        # auto convert umlaut names to punycode
        newcmd = self.__autoIDNConvert(newcmd)

        # request command to API
        cfg = {"CONNECTION_URL": self.__socketURL}
        data = self.getPOSTData(newcmd).encode("UTF-8")
        secured = self.getPOSTData(newcmd, True).encode("UTF-8")
        error = None
        try:
            headers = {"User-Agent": self.getUserAgent()}
            if "REFERER" in self.__curlopts:
                headers["Referer"] = self.__curlopts["REFERER"]
            req = Request(cfg["CONNECTION_URL"], data, headers)
            if "PROXY" in self.__curlopts:
                proxyurl = urlparse(self.__curlopts["PROXY"])
                req.set_proxy(proxyurl.netloc, proxyurl.scheme)
            body = urlopen(req, timeout=self.__socketTimeout).read()
        except Exception as e:
            error = str(e)
            body = rtm.getTemplate("httperror").getPlain()
        r = Response(body, newcmd, cfg)
        if self.__debugMode:
            self.__logger.log(secured, r, error)
        return r

    def requestNextResponsePage(self, rr):
        """
        Request the next page of list entries for the current list query
        Useful for tables
        """
        mycmd = rr.getCommand()
        if "LAST" in mycmd:
            raise Exception(
                "Parameter LAST in use. Please remove it to avoid issues in requestNextPage."
            )
        first = 0
        if "FIRST" in mycmd:
            first = int(mycmd["FIRST"])
        total = rr.getRecordsTotalCount()
        limit = rr.getRecordsLimitation()
        first += limit
        if first < total:
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

    def useHighPerformanceConnectionSetup(self):
        """
        Activate High Performance Setup
        """
        self.setURL(ISPAPI_CONNECTION_URL_PROXY)
        return self

    def useDefaultConnectionSetup(self):
        """
        Activate Default Connection Setup (which is the default anyways)
        """
        self.setURL(ISPAPI_CONNECTION_URL_LIVE)
        return self

    def useOTESystem(self):
        """
        Set OT&E System for API communication
        """
        self.setURL(ISPAPI_CONNECTION_URL_OTE)
        self.__socketConfig.setSystemEntity("1234")
        return self

    def useLIVESystem(self):
        """
        Set LIVE System for API communication (this is the default setting)
        """
        self.setURL(ISPAPI_CONNECTION_URL_LIVE)
        self.__socketConfig.setSystemEntity("54cd")
        return self

    def __flattenCommand(self, cmd):
        """
        Flatten API command to handle it easier later on (nested array for bulk params)
        """
        newcmd = {}
        for key in list(cmd.keys()):
            newKey = key.upper()
            val = cmd[key]
            if val is None:
                continue
            if isinstance(val, list):
                i = 0
                while i < len(val):
                    newcmd[newKey + str(i)] = re.sub(r"[\r\n]", "", str(val[i]))
                    i += 1
            else:
                newcmd[newKey] = re.sub(r"[\r\n]", "", str(val))
        return newcmd

    def __autoIDNConvert(self, cmd):
        """
        Auto convert API command parameters to punycode, if necessary.
        """
        # don't convert for convertidn command to avoid endless loop
        # and ignore commands in string format(even deprecated)
        if isinstance(cmd, str) or re.match(
            r"^CONVERTIDN$", cmd["COMMAND"], re.IGNORECASE
        ):
            return cmd

        toconvert = []
        keys = []
        for key in cmd:
            if re.match(r"^(DOMAIN|NAMESERVER|DNSZONE)([0-9]*)$", key, re.IGNORECASE):
                keys.append(key)
        idxs = []
        for key in keys:
            if not re.match(r"^[a-z0-9.-]+$", cmd[key], re.IGNORECASE):
                toconvert.append(cmd[key])
                idxs.append(key)
        if not toconvert:
            return cmd

        r = self.request({"COMMAND": "ConvertIDN", "DOMAIN": toconvert})
        if r.isSuccess():
            col = r.getColumn("ACE")
            if col is not None:
                for idx, pc in enumerate(col.getData()):
                    cmd[idxs[idx]] = pc
        return cmd
