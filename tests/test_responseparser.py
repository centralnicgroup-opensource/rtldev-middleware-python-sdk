import re
import hexonet.apiconnector.responseparser as RP
from hexonet.apiconnector.responsetemplatemanager import ResponseTemplateManager as RTM


def test_rpmethods():
    rtm = RTM()
    rtm.addTemplate(
        'OK',
        rtm.generateTemplate('200', 'Command completed successfully')
    )

    # #.serialize()
    # [w/ PROPERTY]
    r = rtm.getTemplate('OK').getHash()
    r["PROPERTY"] = {
        "DOMAIN": ['mydomain1.com', 'mydomain2.com', 'mydomain3.com'],
        "RATING": ['1', '2', '3'],
        "SUM": [3]
    }
    assert RP.serialize(r) == (
        '[RESPONSE]\r\nPROPERTY[DOMAIN][0]=mydomain1.com\r\nPROPERTY[DOMAIN' +
        '][1]=mydomain2.com\r\nPROPERTY[DOMAIN][2]=mydomain3.com\r\nPROPERT' +
        'Y[RATING][0]=1\r\nPROPERTY[RATING][1]=2\r\nPROPERTY[RATING][2]=3\r' +
        '\nPROPERTY[SUM][0]=3\r\nCODE=200\r\nDESCRIPTION=Command completed ' +
        'successfully\r\nEOF\r\n'
    )

    # [w/o PROPERTY]
    tpl = rtm.getTemplate('OK')
    assert RP.serialize(tpl.getHash()) == tpl.getPlain()

    # [w/o CODE, w/o DESCRIPTION]
    h = rtm.getTemplate('OK').getHash()
    h.pop('CODE')
    h.pop('DESCRIPTION')
    assert RP.serialize(h) == '[RESPONSE]\r\nEOF\r\n'

    # [w/ QUEUETIME, w/ RUNTIME]
    h = rtm.getTemplate('OK').getHash()
    h["QUEUETIME"] = '0'
    h["RUNTIME"] = '0.12'
    assert RP.serialize(h) == (
        '[RESPONSE]\r\nCODE=200\r\nDESCRIPTION=Command completed successful' +
        'ly\r\nQUEUETIME=0\r\nRUNTIME=0.12\r\nEOF\r\n'
    )
