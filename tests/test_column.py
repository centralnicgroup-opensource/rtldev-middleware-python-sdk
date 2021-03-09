from hexonet.apiconnector.column import Column


def test_columnmethods():
    col = Column("DOMAIN", ["mydomain1.com", "mydomain2.com", "mydomain3.com"])
    assert isinstance(col, Column)
    assert col.getKey() is "DOMAIN"
