from centralnicreseller.apiconnector.socketconfig import SocketConfig


def test_socketconfigmethods():
    d = SocketConfig().getPOSTData()
    assert d is ""
