# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector.responsetemplatemanager
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all functionality to
    manage response templates.
    :copyright: © 2018 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""

import hexonet.apiconnector.responseparser as RP
from hexonet.apiconnector.responsetemplate import ResponseTemplate as RT


class ResponseTemplateManager(object):
    """
    The ResponseTemplateManager class covers all functionality required to manage
    Response Templates.
    """

    # to keep the singleton instance
    __instance = None
    __templates = None

    def __new__(cls):
        if ResponseTemplateManager.__instance is None:
            ResponseTemplateManager.__instance = object.__new__(cls)
        rtm = ResponseTemplateManager.__instance

        ResponseTemplateManager.__templates = {
            "404": rtm.generateTemplate("421", "Page not found"),
            "500": rtm.generateTemplate("500", "Internal server error"),
            "empty": rtm.generateTemplate(
                "423",
                "Empty API response. Probably unreachable API end point {CONNECTION_URL}",
            ),
            "error": rtm.generateTemplate(
                "421", "Command failed due to server error. Client should try again"
            ),
            "expired": rtm.generateTemplate("530", "SESSION NOT FOUND"),
            "httperror": rtm.generateTemplate(
                "421", "Command failed due to HTTP communication error"
            ),
            "invalid": rtm.generateTemplate(
                "423", "Invalid API response. Contact Support"
            ),
            "unauthorized": rtm.generateTemplate("530", "Unauthorized"),
        }
        return rtm

    @staticmethod
    def getInstance():
        """
        Returns the singleton instance
        """
        return ResponseTemplateManager()

    def generateTemplate(self, code, description):
        """
        Returns a response template string for the given code and description
        """
        return ("[RESPONSE]\r\nCODE={0}\r\nDESCRIPTION={1}\r\nEOF\r\n").format(
            code, description
        )

    def addTemplate(self, id, plain):
        """
        Add response template to template container
        """
        self.__templates[id] = plain
        return self.__instance

    def getTemplate(self, id):
        """
        Get response template instance from template container
        """
        if self.hasTemplate(id):
            return RT(self.__templates[id])
        return RT(self.generateTemplate("500", "Response Template not found"))

    def getTemplates(self):
        """
        Return all available response templates
        """
        tpls = {}
        for key in list(self.__templates.keys()):
            tpls[key] = RT(self.__templates[key])
        return tpls

    def hasTemplate(self, id):
        """
        Check if given template exists in template container
        """
        return id in self.__templates

    def isTemplateMatchHash(self, tpl2, id):
        """
        Check if given API response hash matches a given template by code and description
        """
        h = self.getTemplate(id).getHash()
        return (h["CODE"] == tpl2["CODE"]) and (h["DESCRIPTION"] == tpl2["DESCRIPTION"])

    def isTemplateMatchPlain(self, plain, id):
        """
        Check if given API plain response matches a given template by code and description
        """
        h = self.getTemplate(id).getHash()
        tpl2 = RP.parse(plain)
        return (h["CODE"] == tpl2["CODE"]) and (h["DESCRIPTION"] == tpl2["DESCRIPTION"])
