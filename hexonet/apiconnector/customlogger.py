# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector.customlogger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module provides all necessary functionality for
    debug outputs
    :copyright: © 2020 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""

from hexonet.apiconnector.logger import Logger
import sys


class CustomLogger(Logger, object):
    """
    The Logger class covers all you need to cover debug outputs of the API communication.
    """

    def __init__(self):
        """
        constructor calling parent constructor
        """
        super(CustomLogger, self).__init__()

    def log(self, post, r, error):
        """
        output/log given data
        """
        #
        # implement your own logic here
        #
        # print(r.getCommandPlain())
        # print(post)
        # if error:
        #     print("HTTP communication failed: %s" % (error), sys.stderr)
        # print(r.getPlain())
