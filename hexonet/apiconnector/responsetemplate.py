# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector.responsetemplate
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all basic functionality to
    deal with Backend API responses.
    :copyright: © 2018 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""

import hexonet.apiconnector.responseparser as RP


class ResponseTemplate(object):
    """
    The ResponseTemplate class is the base class for the Response Class that
    covers basic functionality to work with Backend API responses.
    """

    def __init__(self, response=""):
        #: Holds the response as plain text / string
        self.__raw = response
        if (response is "") or (response is None):
            self.__raw = "[RESPONSE]\r\nCODE=423\r\nDESCRIPTION=Empty API response\r\nEOF\r\n"

        # try/except to support old versions of python (python2.5)
        try:
            if isinstance(self.__raw, bytes):
                self.__raw = self.__raw.decode("utf-8")
        except UnicodeError:
            self.__raw = self.__raw.decode("latin1")
        except BaseException:
            self.__raw = self.__raw.decode("utf-8")

        if isinstance(response, dict):
            raise TypeError('Type "dict" is not allowed for parameter "response". Use type "string" instead.')
        else:
            #: Holds the response as hash
            self.__hash = RP.parse(self.__raw)

    def getCode(self):
        """
        Returns the API response code as integer
        """
        return int(self.__hash['CODE'])

    def getDescription(self):
        """
        Returns the API response description
        """
        return self.__hash['DESCRIPTION']

    def getPlain(self):
        """
        Returns the plain API response
        """
        return self.__raw

    def getQueuetime(self):
        """
        Get Queuetime of API response as float value
        """
        if ("QUEUETIME" in self.__hash):
            return float(self.__hash["QUEUETIME"])
        return 0.00

    def getHash(self):
        """
        Get API response as Hash
        """
        return self.__hash

    def getRuntime(self):
        """
        Get Runtime of API response as float value
        """
        if ("RUNTIME" in self.__hash):
            return float(self.__hash["RUNTIME"])
        return 0.00

    def isError(self):
        """
        Check if current API response represents an error case (5xx)
        """
        return self.__hash["CODE"][0] == "5"

    def isSuccess(self):
        """
        Check if current API response represents a success case (2xx)
        """
        return self.__hash["CODE"][0] == "2"

    def isTmpError(self):
        """
        Check if current API response represents a temporary error case (4xx)
        """
        return self.__hash["CODE"][0] == "4"
