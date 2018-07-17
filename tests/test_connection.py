from hexonet.apiconnector import connect
from hexonet.apiconnector.connection import Connection


def test_connectcommon():
    api = connect(
        "test.user",
        "test.password",
        "https://coreapi.1api.net/call/call.cgi",
        "1234"
    )
    assert isinstance(api, Connection)
    api.call({
        "COMMAND": "GetUserIndex"
    })


def test_connectuserandrole():
    api = connect(
        "test.user",
        "test.password",
        "https://coreapi.1api.net/call/call.cgi",
        "1234",
        "hexotestman.com",
        "testrole"
    )
    assert isinstance(api, Connection)
    api.call({
        "COMMAND": "GetUserIndex"
    })
