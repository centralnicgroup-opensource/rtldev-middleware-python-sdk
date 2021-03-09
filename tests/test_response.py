from hexonet.apiconnector.response import Response as R
import hexonet.apiconnector.responseparser as RP
from hexonet.apiconnector.responsetemplatemanager import ResponseTemplateManager as RTM
import re


def test_responsemethods():
    rtm = RTM()
    rtm.addTemplate(
        "listP0",
        "[RESPONSE]\r\nPROPERTY[TOTAL][0]=2701\r\nPROPERTY[FIRST][0]=0\r\nP"
        + "ROPERTY[DOMAIN][0]=0-60motorcycletimes.com\r\nPROPERTY[DOMAIN][1]="
        + "0-be-s01-0.com\r\nPROPERTY[COUNT][0]=2\r\nPROPERTY[LAST][0]=1\r\nP"
        + "ROPERTY[LIMIT][0]=2\r\nDESCRIPTION=Command completed successfully"
        + "\r\nCODE=200\r\nQUEUETIME=0\r\nRUNTIME=0.023\r\nEOF\r\n",
    )
    rtm.addTemplate("OK", rtm.generateTemplate("200", "Command completed successfully"))

    # #.getCurrentPageNumber()
    # [w/ entries in response]
    r = R(rtm.getTemplate("listP0").getPlain())
    assert r.getCurrentPageNumber() == 1

    # [w/o entries in response]
    r = R(rtm.getTemplate("OK").getPlain())
    assert r.getCurrentPageNumber() is None

    # #.getFirstRecordIndex()
    # [w/o FIRST in response, no rows]
    r = R(rtm.getTemplate("OK").getPlain())
    assert r.getFirstRecordIndex() is None

    # [w/o FIRST in response, rows]
    h = rtm.getTemplate("OK").getHash()
    h["PROPERTY"] = {"DOMAIN": ["mydomain1.com", "mydomain2.com"]}
    r = R(RP.serialize(h))
    assert r.getFirstRecordIndex() == 0

    # #.constructor [place holder replacements]
    r = R("")
    assert re.search(r"\{[A-Z_]+\}", r.getDescription()) is None

    r = R("", {"COMMAND": "StatusAccount"}, {"CONNECTION_URL": "123HXPHFOUND123"})
    assert re.search(r"123HXPHFOUND123", r.getDescription()) is not None

    # #.getCommandPlain()
    # case 1
    r = R(
        "",
        {
            "COMMAND": "QueryDomainOptions",
            "DOMAIN0": "example.com",
            "DOMAIN1": "example.net",
        },
    )
    expected = (
        "COMMAND = QueryDomainOptions\nDOMAIN0 = example.com\nDOMAIN1 = example.net\n"
    )
    assert r.getCommandPlain() == expected

    # case secured
    r = R(
        "",
        {
            "COMMAND": "CheckAuthentication",
            "PASSWORD": "test.passw0rd",
            "SUBUSER": "test.user",
        },
    )
    expected = "COMMAND = CheckAuthentication\nPASSWORD = ***\nSUBUSER = test.user\n"
    assert r.getCommandPlain() == expected

    # #.getColumns()
    r = R(rtm.getTemplate("listP0").getPlain())
    cols = r.getColumns()
    assert len(cols) == 6

    # #.getColumnIndex()
    # [colum exists]
    r = R(rtm.getTemplate("listP0").getPlain())
    assert r.getColumnIndex("DOMAIN", 0) == "0-60motorcycletimes.com"

    # [colum does not exist]
    assert r.getColumnIndex("COLUMN_NOT_EXISTS", 0) is None

    # #.getColumnKeys()
    colkeys = r.getColumnKeys()
    assert len(colkeys) == 6
    assert sorted(colkeys) == sorted(
        ["COUNT", "DOMAIN", "FIRST", "LAST", "LIMIT", "TOTAL"]
    )

    # #.getCurrentRecord()
    # [records available]
    rec = r.getCurrentRecord()
    assert rec.getData() == {
        "COUNT": "2",
        "DOMAIN": "0-60motorcycletimes.com",
        "FIRST": "0",
        "LAST": "1",
        "LIMIT": "2",
        "TOTAL": "2701",
    }

    # [no records available]
    r = R(rtm.getTemplate("OK").getPlain())
    assert r.getCurrentRecord() is None

    # #.getListHash()
    r = R(rtm.getTemplate("listP0").getPlain())
    lh = r.getListHash()
    assert len(lh["LIST"]) == 2
    assert lh["meta"]["columns"] is r.getColumnKeys()
    assert lh["meta"]["pg"] == r.getPagination()

    # #.getNextRecord()
    rec = r.getNextRecord()
    assert rec.getData() == {"DOMAIN": "0-be-s01-0.com"}
    rec = r.getNextRecord()
    assert rec is None

    # #.getPagination()
    pager = r.getPagination()
    assert sorted(pager.keys()) == sorted(
        [
            "COUNT",
            "CURRENTPAGE",
            "FIRST",
            "LAST",
            "LIMIT",
            "NEXTPAGE",
            "PAGES",
            "PREVIOUSPAGE",
            "TOTAL",
        ]
    )

    # #.getPreviousRecord()
    r.getNextRecord()
    assert r.getPreviousRecord().getData() == {
        "COUNT": "2",
        "DOMAIN": "0-60motorcycletimes.com",
        "FIRST": "0",
        "LAST": "1",
        "LIMIT": "2",
        "TOTAL": "2701",
    }
    assert r.getPreviousRecord() is None

    # #.hasNextPage()
    # [no rows]
    r = R(rtm.getTemplate("OK").getPlain())
    assert r.hasNextPage() is False

    # [rows]
    r = R(rtm.getTemplate("listP0").getPlain())
    assert r.hasNextPage() is True

    # #.hasPreviousPage()
    # [no rows]
    r = R(rtm.getTemplate("OK").getPlain())
    assert r.hasPreviousPage() is False

    # [rows]
    r = R(rtm.getTemplate("listP0").getPlain())
    assert r.hasPreviousPage() is False

    # #.getLastRecordIndex()
    # [no rows]
    r = R(rtm.getTemplate("OK").getPlain())
    assert r.getLastRecordIndex() is None

    # [rows]
    h = rtm.getTemplate("OK").getHash()
    h["PROPERTY"] = {"DOMAIN": ["mydomain1.com", "mydomain2.com"]}
    r = R(RP.serialize(h))
    assert r.getLastRecordIndex() == 1

    # #.getNextPageNumber()
    # [no rows]
    r = R(rtm.getTemplate("OK").getPlain())
    assert r.getNextPageNumber() is None

    # [rows]
    r = R(rtm.getTemplate("listP0").getPlain())
    assert r.getNextPageNumber() == 2

    # #.getNumberOfPages()
    r = R(rtm.getTemplate("OK").getPlain())
    assert r.getNumberOfPages() == 0

    # #.getPreviousPageNumber()
    # [no rows]
    r = R(rtm.getTemplate("OK").getPlain())
    assert r.getPreviousPageNumber() is None

    # [rows]
    r = R(rtm.getTemplate("listP0").getPlain())
    assert r.getPreviousPageNumber() is None

    # #.rewindRecordList()
    r = R(rtm.getTemplate("listP0").getPlain())
    assert r.getPreviousRecord() is None
    assert r.getNextRecord() is not None
    assert r.getNextRecord() is None
    assert r.rewindRecordList().getPreviousRecord() is None
