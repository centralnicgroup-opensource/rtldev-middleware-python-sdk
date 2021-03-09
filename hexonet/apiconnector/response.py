# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector.response
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all necessary functionality to
    work with Backend API responses.
    :copyright: © 2018 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""
from hexonet.apiconnector.responsetemplate import ResponseTemplate as RT
from hexonet.apiconnector.column import Column
from hexonet.apiconnector.record import Record

import math
import re


class Response(RT, object):
    """
    The Response class covers all necessary functionality to cover access to
    Backend API response data in a useful way.
    """

    def __init__(self, raw, cmd=None, cfg={}):
        super(Response, self).__init__(raw)

        if re.search(r"\{[A-Z_]+\}", self._raw):
            for key, value in cfg.items():
                self._raw = self._raw.replace("{%s}" % (key), value)
            self._raw = re.sub(r"\{[A-Z_]+\}", "", self._raw)
            super(Response, self).__init__(self._raw)

        # The API Command used within this request
        self.__command = cmd
        if (self.__command is not None) and ("PASSWORD" in self.__command):
            self.__command["PASSWORD"] = "***"
        # Column names available in this responsse.
        # NOTE: this includes also FIRST, LAST, LIMIT, COUNT, TOTAL
        # and maybe further specific columns in case of a list query
        self.__columnkeys = []
        # Container of Column Instances
        self.__columns = []
        # Record Index we currently point to in record list
        self.__recordIndex = 0
        # Record List (List of rows)
        self.__records = []

        h = self.getHash()
        if "PROPERTY" in h:
            colKeys = list(h["PROPERTY"].keys())
            count = 0
            for c in colKeys:
                d = h["PROPERTY"][c]
                self.addColumn(c, d)
                mylen = len(d)
                if mylen > count:
                    count = mylen
            for i in range(count):
                d = {}
                for k in colKeys:
                    col = self.getColumn(k)
                    if col is not None:
                        v = col.getDataByIndex(i)
                        if v is not None:
                            d[k] = v
                self.addRecord(d)

    def addColumn(self, key, data):
        """
        Add a column to the column list
        """
        col = Column(key, data)
        self.__columns.append(col)
        self.__columnkeys.append(key)
        return self

    def addRecord(self, h):
        """
        Add a record to the record list
        """
        self.__records.append(Record(h))
        return self

    def getColumn(self, key):
        """
        Get column by column name
        """
        if self.__hasColumn(key):
            return self.__columns[self.__columnkeys.index(key)]
        return None

    def getColumnIndex(self, colkey, index):
        """
        Get Data by Column Name and Index
        """
        col = self.getColumn(colkey)
        return col.getDataByIndex(index) if (col is not None) else None

    def getColumnKeys(self):
        """
        Get Column Names
        """
        return self.__columnkeys

    def getColumns(self):
        """
        Get List of Columns
        """
        return self.__columns

    def getCommand(self):
        """
        Get Command used in this request
        """
        return self.__command

    def getCommandPlain(self):
        """
        Get Command used in this request in plain text
        """
        tmp = ""
        for key, val in self.__command.items():
            tmp += "%s = %s\n" % (key, val)
        return tmp

    def getCurrentPageNumber(self):
        """
        Get Page Number of current List Query
        """
        first = self.getFirstRecordIndex()
        limit = self.getRecordsLimitation()
        if (first is not None) and (limit):
            return math.floor(first / limit) + 1
        return None

    def getCurrentRecord(self):
        """
        Get Record of current record index
        """
        return (
            self.__records[self.__recordIndex] if (self.__hasCurrentRecord()) else None
        )

    def getFirstRecordIndex(self):
        """
        Get Index of first row in this response
        """
        col = self.getColumn("FIRST")
        if col is not None:
            f = col.getDataByIndex(0)
            if f is not None:
                return int(f)
        if len(self.__records):
            return 0
        return None

    def getLastRecordIndex(self):
        """
        Get last record index of the current list query
        """
        col = self.getColumn("LAST")
        if col is not None:
            data = col.getDataByIndex(0)
            if data is not None:
                return int(data)
        len = self.getRecordsCount()
        if len:
            return len - 1
        return None

    def getListHash(self):
        """
        Get Response as List Hash including useful meta data for tables
        """
        lh = []
        for rec in self.getRecords():
            lh.append(rec.getData())
        return {
            "LIST": lh,
            "meta": {"columns": self.getColumnKeys(), "pg": self.getPagination()},
        }

    def getNextRecord(self):
        """
        Get next record in record list
        """
        if self.__hasNextRecord():
            self.__recordIndex += 1
            return self.__records[self.__recordIndex]
        return None

    def getNextPageNumber(self):
        """
        Get Page Number of next list query
        """
        cp = self.getCurrentPageNumber()
        if cp is None:
            return None
        page = cp + 1
        pages = self.getNumberOfPages()
        return page if (page <= pages) else pages

    def getNumberOfPages(self):
        """
        Get the number of pages available for this list query
        """
        t = self.getRecordsTotalCount()
        limit = self.getRecordsLimitation()
        if t and limit:
            return math.ceil(t / self.getRecordsLimitation())
        return 0

    def getPagination(self):
        """
        Get object containing all paging data
        """
        return {
            "COUNT": self.getRecordsCount(),
            "CURRENTPAGE": self.getCurrentPageNumber(),
            "FIRST": self.getFirstRecordIndex(),
            "LAST": self.getLastRecordIndex(),
            "LIMIT": self.getRecordsLimitation(),
            "NEXTPAGE": self.getNextPageNumber(),
            "PAGES": self.getNumberOfPages(),
            "PREVIOUSPAGE": self.getPreviousPageNumber(),
            "TOTAL": self.getRecordsTotalCount(),
        }

    def getPreviousPageNumber(self):
        """
        Get Page Number of previous list query
        """
        cp = self.getCurrentPageNumber()
        if cp is not None:
            cp = cp - 1
            if cp:
                return cp
        return None

    def getPreviousRecord(self):
        """
        Get previous record in record list
        """
        if self.__hasPreviousRecord():
            self.__recordIndex -= 1
            return self.__records[self.__recordIndex]
        return None

    def getRecord(self, idx):
        """
        Get Record at given index
        """
        if idx >= 0 and len(self.__records) > idx:
            return self.__records[idx]
        return None

    def getRecords(self):
        """
        Get all Records
        """
        return self.__records

    def getRecordsCount(self):
        """
        Get count of rows in this response
        """
        return len(self.__records)

    def getRecordsTotalCount(self):
        """
        Get total count of records available for the list query
        """
        col = self.getColumn("TOTAL")
        if col is not None:
            t = col.getDataByIndex(0)
            if t is not None:
                return int(t)
        return self.getRecordsCount()

    def getRecordsLimitation(self):
        """
        Get limit(ation) setting of the current list query
        """
        col = self.getColumn("LIMIT")
        if col is not None:
            data = col.getDataByIndex(0)
            if data is not None:
                return int(data)
        return self.getRecordsCount()

    def hasNextPage(self):
        """
        Check if this list query has a next page
        """
        cp = self.getCurrentPageNumber()
        if cp is None:
            return False
        return (cp + 1) <= self.getNumberOfPages()

    def hasPreviousPage(self):
        """
        Check if this list query has a previous page
        """
        cp = self.getCurrentPageNumber()
        if cp is None:
            return False
        return (cp - 1) > 0

    def rewindRecordList(self):
        """
        Reset index in record list back to zero
        """
        self.__recordIndex = 0
        return self

    def __hasColumn(self, key):
        """
        Check if column exists in response
        """
        try:
            self.__columnkeys.index(key)
        except ValueError:
            return False
        return True

    def __hasCurrentRecord(self):
        """
        Check if the record list contains a record for the
        current record index in use
        """
        tlen = len(self.__records)
        return tlen > 0 and self.__recordIndex >= 0 and self.__recordIndex < tlen

    def __hasNextRecord(self):
        """
        Check if the record list contains a next record for the
        current record index in use
        """
        next = self.__recordIndex + 1
        return self.__hasCurrentRecord() and (next < len(self.__records))

    def __hasPreviousRecord(self):
        """
        Check if the record list contains a previous record for the
        current record index in use
        """
        return self.__recordIndex > 0 and self.__hasCurrentRecord()
