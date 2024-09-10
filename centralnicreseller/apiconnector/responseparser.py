# -*- coding: utf-8 -*-
"""
    centralnicreseller.apiconnector.responseparser
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module covers all necessary functionality to
    parse a raw Backend API response and to serialize it back.
    :copyright: © 2024 Team Internet Group PLC.
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