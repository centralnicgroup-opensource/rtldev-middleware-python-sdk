# -*- coding: utf-8 -*-
"""
    centralnicreseller.apiconnector.record
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all necessary functionality to
    work with a record and wrapped data.
    :copyright: © 2024 Team Internet Group PLC.
    :license: MIT, see LICENSE for more details.
"""


class Record(object):
    """
    The Record class covers all you need to access record data of a Backend API response.
    """

    def __init__(self, data):
        self.__data = data

    def getData(self):
        """
        get row data
        """
        return self.__data

    def getDataByKey(self, key):
        """
        get row data for given column name
        """
        if self.__hasData(key):
            return self.__data[key]
        return None

    def __hasData(self, key):
        """
        check if record has data for given column name
        """
        return key in self.__data
