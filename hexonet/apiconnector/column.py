# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector.column
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all necessary functionality to
    work with a column and wrapped data.
    :copyright: © 2018 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""


class Column(object):
    """
    The Column class covers all you need to access column data of a Backend API response.
    """

    def __init__(self, key, data):
        self.__key = key
        self.__data = data
        self.length = len(data)

    def getKey(self):
        """
        Get column name
        """
        return self.__key

    def getData(self):
        """
        Get column data
        """
        return self.__data

    def getDataByIndex(self, idx):
        """
        Get column data at given index
        """
        return self.__data[idx] if self.hasDataIndex(idx) else None

    def hasDataIndex(self, idx):
        """
        Check if column has a given data index
        """
        return True if ((idx >= 0) and (idx < self.length)) else False
