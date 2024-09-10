# -*- coding: utf-8 -*-
"""
    centralnicreseller.apiconnector.socketconfig
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all necessary functionality to
    pre-configure http communication with our Backend System.
    :copyright: © 2024 Team Internet Group PLC.
    :license: MIT, see LICENSE for more details.
"""

from urllib.parse import quote, unquote


class SocketConfig(object):
    """
    The SocketConfig class helps to configure the http communcation with our Backend System.
    """

    def __init__(self):
        # account name
        self.__login = None
        # account password
        self.__pw = None
        # API session id
        self.__sessionid = None
        # API persistent connection for session
        self.__persistent = None

    def getPOSTData(self):
        """
        Create POST data string out of connection data
        """
        data = []
        tpl = "{0}={1}&"
        keys = ["__login", "__pw", "__sessionid", "__persistent"]

        for key in keys:
            item = getattr(self, "_SocketConfig" + key)
            if item:
                if key == "__persistent":
                    data.append(tpl.format(quote(key[2:]), quote(item)))
                else:
                    data.append(tpl.format(quote("s_" + key[2:]), quote(item)))

        return "".join(data)

    def getSession(self):
        """
        Get API Session ID in use
        """
        return self.__sessionid

    def getLogin(self):
        """
        get account login to use
        """
        return self.__login

    def setLogin(self, value):
        """
        Set account name to use
        """
        self.__login = value
        return self

    def setPassword(self, value):
        """
        Set account password to use
        """
        self.__sessionid = None
        self.__pw = value
        return self

    def setSession(self, value):
        """
        Set API Session ID to use
        """
        self.__pw = None
        self.__persistent = None
        self.__sessionid = value
        return self

    def setPersistent(self):
        """
        Set API persistent connection for session
        """
        self.__sessionid = None
        self.__persistent = "1"
        return self
