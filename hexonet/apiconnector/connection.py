# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector.connection
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module implements the API connector class.
    :copyright: © 2018 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""

from six.moves.urllib.request import urlopen
from six.moves.urllib.parse import urlparse, urlencode
import hexonet.apiconnector.util
from hexonet.apiconnector.response import Response


class Connection:
    """The hexonet.apiconnector implements a communication API for the
    insanely fast HEXONET Backend API.
    The Connection class is the entry point of this communication and
    covers all necessary client functionality.
    An Instance can be created by using the :func:`connect` method defined
    in :file:`__init__.py` e.g.::
        import hexonet.apiconnector
        api = hexonet.apiconnector.connect(
            "test.user",
            "test.passw0rd",
            "https://coreapi.1api.net/api/call.cgi",
            "1234"
            //,"hexotestman.com" //subuser view
            //,"testrole" //specify a role user
        );
    or in the usual way e.g.::
        from hexonet.apiconnector.connection import Connection as HXClient
        api = HXClient({
            "login": "test.user",
            "password": "test.passw0rd",
            "url": "https://coreapi.1api.net/api/call.cgi",
            "entity": "1234",
            //"user": "hexotestman.com",//subuser view
            //"role": "testrole",//specify a role user
        });
    :param config: the configuration object, use the following keys.
                   login    -> your account / user name to use
                   password -> your account password
                   url      -> the Backend API url to use, please use "https://coreapi.1api.net/api/call.cgi"
                   entity   -> the Backend API system entity: use "1234" for OT&E and "54cd" for LIVE system
                   user     -> subuser account / user name for a subuser data view
                   role     -> a role user to use (located directly under your account / user name)
    """

    def __init__(self, config):
        #: Holds the configuration object.
        #: .. versionadded:: 1.0.0
        self.__config = config

    def call_raw_http(self, command, config=None):
        """
        Make a curl API call over HTTP(S) and returns the response as a string
        .. versionadded:: 1.0.0
        """
        post = {}
        if ('login' in self.__config):
            post['s_login'] = self.__config['login']
        if ('password' in self.__config):
            post['s_pw'] = self.__config['password']
        if ('entity' in self.__config):
            post['s_entity'] = self.__config['entity']
        if ('user' in self.__config):
            post['s_user'] = self.__config['user']
        if ('role' in self.__config):
            post['s_login'] = self.__config['login'] + "!" + self.__config['role']

        post['s_command'] = hexonet.apiconnector.util.command_encode(command)
        post = urlencode(post)
        response = urlopen(self.__config['url'], post.encode('UTF-8'))
        content = response.read()
        return content

    def call_raw(self, command, config=None):
        """
        Make a curl API call and returns the response as a string
        .. versionadded:: 1.0.0
        """
        return self.call_raw_http(command, config)

    def call(self, command, config=None):
        """
        Make a curl API call and returns the response as a hexonet.apiconnector.Response
        .. versionadded:: 1.0.0
        """
        return Response(self.call_raw(command, config))
