# -*- coding: utf-8 -*-
"""
    hexonet.apiconnector.responseparser
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all necessary functionality to
    parse a raw Backend API response and to serialize it back.
    :copyright: © 2018 by HEXONET GmbH.
    :license: MIT, see LICENSE for more details.
"""

import re


def parse(raw):
    """
    Returns the response as a string
    """
    r = {}
    re1 = re.compile(r"^([^\=]*[^\t\= ])[\t ]*=[\t ]*(.*)$")
    re2 = re.compile(r"^property\[([^\]]*)\]", re.IGNORECASE)

    raw = raw.replace("\r\n", "\n")
    for line in raw.split("\n"):
        m1 = re1.match(line)
        if not m1:
            continue
        attr = m1.group(1)
        value = m1.group(2)
        value = re.sub(r"[\t ]*$", "", value)

        m2 = re2.match(attr)
        if m2:
            prop = m2.group(1).upper()
            prop = re.sub(r"\s", "", prop)
            if "PROPERTY" not in r:
                r["PROPERTY"] = {}
            if prop not in r["PROPERTY"]:
                r["PROPERTY"][prop] = []
            r["PROPERTY"][prop].append(value)
        else:
            r[attr.upper()] = value
    return r


def serialize(r):
    """
    Returns the dictionary represenation serialized back to plain text
    """
    d = ""
    if "PROPERTY" in r:
        keys = sorted(r["PROPERTY"].keys())
        for key in keys:
            for index, val in enumerate(r["PROPERTY"][key]):
                d += ("\r\nPROPERTY[{0}][{1}]={2}").format(key, index, val)
    for prop in ["CODE", "DESCRIPTION", "QUEUETIME", "RUNTIME"]:
        if prop in r:
            d += ("\r\n{0}={1}").format(prop, r[prop])
    return ("[RESPONSE]{0}\r\nEOF\r\n").format(d)
