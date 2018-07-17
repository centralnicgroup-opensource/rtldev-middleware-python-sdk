# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector.response
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all necessary functionality to
    work with Backend API responses.
    :copyright: © 2018 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""
import hexonet.apiconnector.util


class Response:
    """The hexonet.apiconnector implements a communication API for the
    insanely fast HEXONET Backend API.
    The Response class is what you get from Connection object's call method
    which is the default function to use for API requests.
    See :file:`connection.py`, :meth:`~hexonet.apiconnector.connection.Connection.call`
    An Instance can be created in the usual way e.g.::
        r = Response("[RESPONSE]\r\ncode=530\r\ndescription=Unauthorized\r\nEOF\r\n");
    :param response: the plain Backend API response test.
    """

    def __init__(self, response):
        #: Holds the response as plain text / string
        #: .. versionadded:: 1.0.0
        self._response_string = None
        #: Holds the response as hash
        #: .. versionadded:: 1.0.0
        self._response_hash = None
        #: Holds the response as plain list hash
        #: .. versionadded:: 1.0.0
        self._response_list_hash = None

        # try/except to support old versions of python (python2.5)
        try:
            if isinstance(response, bytes):
                response = response.decode("utf-8")
                self._response_string = response
        except UnicodeError:
            response = response.decode("latin1")
            self._response_string = response
        except BaseException:
            response = response.decode("utf-8")
            self._response_string = response

        if isinstance(response, dict):
            self._response_hash = response

    def as_string(self):
        """
        Returns the response as a string
        .. versionadded:: 1.0.0
        """
        return self._response_string

    def as_hash(self):
        """
        Returns the response as a hash
        .. versionadded:: 1.0.0
        """
        if self._response_hash is None:
            self._response_hash = hexonet.apiconnector.util.response_to_hash(self._response_string)
        return self._response_hash

    def as_list_hash(self):
        """
        Returns the response as a list hash
        .. versionadded:: 1.0.0
        """
        if self._response_list_hash is None:
            self._response_list_hash = hexonet.apiconnector.util.response_to_list_hash(self.as_hash())
        return self._response_list_hash

    def as_list(self):
        """
        Returns the response as a list
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["ITEMS"]

    def __len__(self):
        """
        Returns the number of items
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["COUNT"]

    def __getitem__(self, index):
        """
        Returns the item for the given index
        .. versionadded:: 1.0.0
        """
        if isinstance(index, int):
            return self.as_list()[index]
        if isinstance(index, str):
            return self.as_hash()[index]
        pass

    def code(self):
        """
        Returns the response code
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["CODE"]

    def description(self):
        """
        Returns the response description
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["DESCRIPTION"]

    def runtime(self):
        """
        Returns the response runtime
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["RUNTIME"]

    def queuetime(self):
        """
        Returns the response queuetime
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["QUEUETIME"]

    def properties(self):
        """
        Returns the response properties
        .. versionadded:: 1.0.0
        """
        return self.as_hash()["PROPERTY"]

    def property(self, index=None):
        """
        Returns the property for a given index
        If no index given, the complete property list is returned
        .. versionadded:: 1.0.0
        """
        properties = self.properties()
        if index:
            try:
                return properties[index]
            except BaseException:
                return None
        else:
            return properties

    def is_success(self):
        """
        Returns true if the results is a success
        Success = response code starting with 2
        .. versionadded:: 1.0.0
        """
        if str(self.code()).startswith("2"):
            return True
        else:
            return False

    def is_tmp_error(self):
        """
        Returns true if the results is a tmp error
        tmp error = response code starting with 4
        .. versionadded:: 1.0.0
        """
        if str(self.code()).startswith("4"):
            return True
        else:
            return False

    def columns(self):
        """
        Returns the columns
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["COLUMNS"]

    def first(self):
        """
        Returns the index of the first element
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["FIRST"]

    def last(self):
        """
        Returns the index of the last element
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["LAST"]

    def count(self):
        """
        Returns the number of list elements returned (= last - first + 1)
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["COUNT"]

    def limit(self):
        """
        Returns the limit of the response
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["LIMIT"]

    def total(self):
        """
        Returns the total number of elements found (!= count)
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["TOTAL"]

    def pages(self):
        """
        Returns the number of pages
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["PAGES"]

    def page(self):
        """
        Returns the number of the current page (starts with 1)
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["PAGE"]

    def prevpage(self):
        """
        Returns the number of the previous page
        .. versionadded:: 1.0.0
        """
        try:
            return self.as_list_hash()["PREVPAGE"]
        except BaseException:
            return None

    def prevpagefirst(self):
        """
        Returns the first index for the previous page
        .. versionadded:: 1.0.0
        """
        try:
            return self.as_list_hash()["PREVPAGEFIRST"]
        except BaseException:
            return None

    def nextpage(self):
        """
        Returns the number of the next page
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["NEXTPAGE"]

    def nextpagefirst(self):
        """
        Returns the first index for the next page
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["NEXTPAGEFIRST"]

    def lastpagefirst(self):
        """
        Returns the first index for the last page
        .. versionadded:: 1.0.0
        """
        return self.as_list_hash()["LASTPAGEFIRST"]
