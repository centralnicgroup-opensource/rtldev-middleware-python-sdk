from hexonet.apiconnector.responsetemplate import ResponseTemplate


def test_responsetemplatemethods():
    # check instance [raw empty string]
    tpl = ResponseTemplate()
    assert tpl.getCode() == 423
    assert tpl.getDescription() == 'Empty API response'

    # #.getHash
    h = tpl.getHash()
    assert h["CODE"] == '423'
    assert h["DESCRIPTION"] == 'Empty API response'

    # #.getQueuetime
    # [not in api response]
    assert tpl.getQueuetime() == 0.00
    # [in api response]
    tpl2 = ResponseTemplate(
        '[RESPONSE]\r\ncode=423\r\ndescription=Empty API response\r\nqueuetime=0\r\nruntime=0.12\r\nEOF\r\n')
    assert tpl2.getQueuetime() == 0.00

    # #.getRuntime
    # [not in api response]
    assert tpl.getRuntime() == 0.00
    # [in api response]
    assert tpl2.getRuntime() == 0.12

    # #.isPending
    # [not in api response]
    assert tpl.isPending() == False
    # [in api response]
    tpl2 = ResponseTemplate(
        '[RESPONSE]\r\ncode=423\r\ndescription=Empty API response\r\npending=1\r\nEOF\r\n')
    assert tpl2.isPending()
