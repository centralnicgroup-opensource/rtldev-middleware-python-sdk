from hexonet.apiconnector import connect
from hexonet.apiconnector.util import sqltime, timesql, url_encode, url_decode, base64_encode, base64_decode


def test_utilmethods():
    # cover COLUMN specific code in response_to_list_hash
    # LINE 108-109 deprecated?
    api = connect(
        "test.user",
        "test.passw0rd",
        "https://coreapi.1api.net/api/call.cgi",
        "1234"
    )
    response = api.call({
        "COMMAND": "QueryDomainPendingDeleteList",
        "ZONE": ["COM", "NET"],
        "LIMIT": 10,
        "FIRST": 20
    })
    assert response.code() == 200

    # sqltime()
    ts = sqltime()  # now()
    assert isinstance(ts, str)

    uxorg = 1531479459
    ts = sqltime(uxorg)
    assert isinstance(ts, str)
    assert ts == "2018-07-13 12:57:39"

    # timesql()
    ux = timesql(ts)
    assert ux == uxorg

    # url_encode / url_decode
    enc = url_encode("+")
    assert enc == "%2B"

    dec = url_decode("%2B")
    assert dec == "+"

    # base64_encode / base64_decode
    key = b"das stinkt zum Himmel"
    enc = base64_encode(key)
    assert enc == b"ZGFzIHN0aW5rdCB6dW0gSGltbWVs"
    assert base64_decode(enc) == key
