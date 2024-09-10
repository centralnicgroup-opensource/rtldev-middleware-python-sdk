# -*- coding: utf-8 -*-
"""
    centralnicreseller.apiconnector.logger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module provides all necessary functionality for
    debug outputs see the customlogger class on how to override this
    :copyright: © 2024 Team Internet Group PLC.
    :license: MIT, see LICENSE for more details.
"""

import sys


class Logger(object):
    """
    The Logger class covers all you need to cover debug outputs of the API communication.
    """

    def log(self, post, r, error):
        """
        output/log given data
        """
        print(r.getCommandPlain())
        print(post)
        if error:
            print("HTTP communication failed: %s" % (error), sys.stderr)
        print(r.getPlain())
