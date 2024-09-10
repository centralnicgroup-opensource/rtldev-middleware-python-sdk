from centralnicreseller.apiconnector.responsetemplate import ResponseTemplate


def test_responsetemplatemethods():
    # check invalid api response
    tpl = ResponseTemplate("[RESPONSE]\r\nqueuetime = 0\r\nEOF\r\n")
    assert tpl.getCode() == 423
    assert tpl.getDescription() == "Invalid API response. Contact Support"

    descr = "Empty API response. Probably unreachable API end point {CONNECTION_URL}"
    # check instance [raw empty string]
    tpl = ResponseTemplate()
    assert tpl.getCode() == 423
    assert tpl.getDescription() == descr

    # #.getHash
    h = tpl.getHash()
    assert h["CODE"] == "423"
    assert h["DESCRIPTION"] == descr

    # #.getQueuetime
    # [not in api response]
    assert tpl.getQueuetime() == 0.00
    # [in api response]
    tpl2 = ResponseTemplate(
        "[RESPONSE]\r\ncode = 423\r\ndescription = %s\r\nqueuetime = 0\r\nruntime = 0.12\r\nEOF\r\n"
        % (descr)
    )
    assert tpl2.getQueuetime() == 0.00

    # #.getRuntime
    # [not in api response]
    assert tpl.getRuntime() == 0.00
    # [in api response]
    assert tpl2.getRuntime() == 0.12