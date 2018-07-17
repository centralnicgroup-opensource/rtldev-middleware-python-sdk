# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector
    ~~~~~~~~~~~~~~~~~~~~
    A connector library for the insanely fast
    HEXONET Backend API.
    :copyright: © 2018 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""
from hexonet.apiconnector.connection import Connection
from hexonet.apiconnector.response import Response

__version__ = '1.2.7'
name = "hexonet.apiconnector"


def connect(login=None, password=None, url=None, entity=None, user=None, role=None, config=None):
    """
    Returns an instance of hexonet.apiconnector.Connection::
        api = connect(
            "test.user",
            "test.passw0rd",
            "https://coreapi.1api.net/api/call.cgi",
            "1234"
            //,"hexotestman.com" //subuser view
            //,"testrole" //specify a role user
        );
    .. versionadded:: 1.0.0
    """

    if config is None:
        config = {}
    if login is not None:
        config['login'] = login
    if password is not None:
        config['password'] = password
    if url is not None:
        config['url'] = url
    if entity is not None:
        config['entity'] = entity
    if user is not None:
        config['user'] = user
    if role is not None:
        config['role'] = role
    return Connection(config)
