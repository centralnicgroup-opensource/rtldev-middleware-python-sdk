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
        self._raw = response
        if (response is "") or (response is None):
            descr = "Empty API response. Probably unreachable API end point {CONNECTION_URL}"
            self._raw = "[RESPONSE]\r\nCODE=423\r\nDESCRIPTION=%s\r\nEOF\r\n" % (descr)

        # try/except to support old versions of python (python2.5)
        try:
            if isinstance(self._raw, bytes):
                self._raw = self._raw.decode("utf-8")
        except UnicodeError:
            self._raw = self._raw.decode("latin1")
        except BaseException:
            self._raw = self._raw.decode("utf-8")

        if isinstance(response, dict):
            raise TypeError(
                'Type "dict" is not allowed for parameter "response". Use type "string" instead.'
            )
        else:
            #: Holds the response as hash
            self.__hash = RP.parse(self._raw)

        if ("CODE" not in self.__hash) or ("DESCRIPTION" not in self.__hash):
            self._raw = "[RESPONSE]\r\nCODE=423\r\nDESCRIPTION=Invalid API response. Contact Support\r\nEOF\r\n"
            self.__hash = RP.parse(self._raw)

    def getCode(self):
        """
        Returns the API response code as integer
        """
        return int(self.__hash["CODE"])

    def getDescription(self):
        """
        Returns the API response description
        """
        return self.__hash["DESCRIPTION"]

    def getPlain(self):
        """
        Returns the plain API response
        """
        return self._raw

    def getQueuetime(self):
        """
        Get Queuetime of API response as float value
        """
        if "QUEUETIME" in self.__hash:
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
        if "RUNTIME" in self.__hash:
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

    def isPending(self):
        """
        Check if current operation is returned as pending
        """
        if "PENDING" in self.__hash:
            return self.__hash["PENDING"] == "1"
        return False
