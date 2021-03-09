from hexonet.apiconnector.record import Record


def test_recordmethods():
    data = {"DOMAIN": "mydomain.com", "RATING": "1", "RNDINT": "321", "SUM": "1"}
    rec = Record(data)
    assert isinstance(rec, Record)
    assert rec.getData() is data
    assert rec.getDataByKey("KEYNOTEXISTING") is None
