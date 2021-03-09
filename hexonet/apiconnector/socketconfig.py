# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector.socketconfig
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all necessary functionality to
    pre-configure http communication with our Backend System.
    :copyright: © 2018 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""

from urllib.parse import quote, unquote


class SocketConfig(object):
    """
    The SocketConfig class helps to configure the http communcation with our Backend System.
    """

    def __init__(self):
        # API system entity. "54cd" for LIVE system; "1234" for OT&E system
        self.__entity = None
        # account name
        self.__login = None
        # one time password (2FA)
        self.__otp = None
        # account password
        self.__pw = None
        # remote ip address (ip filter)
        self.__remoteaddr = None
        # API session id
        self.__session = None
        # subuser account name (subuser specific data view)
        self.__user = None

    def getPOSTData(self):
        """
        Create POST data string out of connection data
        """
        data = ""
        tpl = "{0}={1}&"
        for key in [
            "__entity",
            "__login",
            "__otp",
            "__pw",
            "__remoteaddr",
            "__session",
            "__user",
        ]:
            item = getattr(self, "_SocketConfig" + key)
            if item is not None and item is not "":
                data += tpl.format(quote("s_" + key[2:]), quote(item))
        return data

    def getSession(self):
        """
        Get API Session ID in use
        """
        return self.__session

    def getSystemEntity(self):
        """
        Get API System Entity in use
        """
        return self.__entity

    def setLogin(self, value):
        """
        Set account name to use
        """
        self.__session = None
        self.__login = value
        return self

    def setOTP(self, value):
        """
        Set one time password to use
        """
        self.__session = None
        self.__otp = value
        return self

    def setPassword(self, value):
        """
        Set account password to use
        """
        self.__session = None
        self.__pw = value
        return self

    def setRemoteAddress(self, value):
        """
        Set Remote IP Address to use
        """
        self.__remoteaddr = value
        return self

    def setSession(self, value):
        """
        Set API Session ID to use
        """
        self.__login = None
        self.__pw = None
        self.__otp = None
        self.__session = value
        return self

    def setSystemEntity(self, value):
        """
        Set API System Entity to use. This is set to 54cd / LIVE System by default.
        """
        self.__entity = value
        return self

    def setUser(self, value):
        """
        Set subuser account name (for subuser data view)
        """
        self.__user = value
        return self
