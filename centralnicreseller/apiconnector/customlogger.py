# -*- coding: utf-8 -*-
"""
    centralnicreseller.apiconnector.customlogger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module provides all necessary functionality for
    debug outputs
    :copyright: © 2024 Team Internet Group PLC.
    :license: MIT, see LICENSE for more details.
"""

from centralnicreseller.apiconnector.logger import Logger
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
        super().log(post, r, error)  # Call the parent log method

        # Implement your own logic here
        # For example, you can uncomment the following lines to print additional information
        # print(r.getCommandPlain())
        # print(post)
        # if error:
        #     print("HTTP communication failed: %s" % (error), file=sys.stderr)
        # print(r.getPlain())
