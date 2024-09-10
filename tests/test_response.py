from centralnicreseller.apiconnector.response import Response as R
import centralnicreseller.apiconnector.responseparser as RP
from centralnicreseller.apiconnector.responsetemplatemanager import ResponseTemplateManager as RTM
import re


def test_responsemethods():
    rtm = RTM()
    rtm.addTemplate(
        "listP0",
        "[RESPONSE]\r\nproperty[total][0] = 4\r\nproperty[first][0] = 0\r\nproperty[domain][0] = cnic-ssl-test1.com\r\nproperty[domain][1] = cnic-ssl-test2.com\r\nproperty[count][0] = 2\r\nproperty[last][0] = 1\r\nproperty[limit][0] = 2\r\ndescription = Command completed successfully\r\ncode = 200\r\nqueuetime = 0\r\nruntime = 0.007\r\nEOF\r\n",
    )
    rtm.addTemplate(
        "pendingRegistration",
        "[RESPONSE]\r\ncode = 200\r\ndescription = Command completed successfully\r\nruntime = 0.44\r\nqueuetime = 0\r\n\r\nproperty[status][0] = REQUESTED\r\nproperty[updated date][0] = 2023-05-22 12:14:31.0\r\nproperty[zone][0] = se\r\nEOF\r\n",
    )
    rtm.addTemplate("OK", rtm.generateTemplate(
        "200", "Command completed successfully"))

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

    # #.constructor [place holder replacements]
    r = R("")
    assert re.search(r"\{[A-Z_]+\}", r.getDescription()) is None

    r = R("", {"COMMAND": "StatusAccount"}, {
          "CONNECTION_URL": "123HXPHFOUND123"})
    assert re.search(r"123HXPHFOUND123", r.getDescription()) is not None

    # #.getCommandPlain()
    # case 1
    r = R(
        "",
        {
            "COMMAND": "CheckDomains",
            "DOMAIN0": "example.com",
            "DOMAIN1": "example.net",
        },
    )
    expected = (
        "COMMAND = CheckDomains\nDOMAIN0 = example.com\nDOMAIN1 = example.net\n"
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
    assert r.getColumnIndex("DOMAIN", 0) == "cnic-ssl-test1.com"

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
        "DOMAIN": "cnic-ssl-test1.com",
        "FIRST": "0",
        "LAST": "1",
        "LIMIT": "2",
        "TOTAL": "4",
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
    assert rec.getData() == {"DOMAIN": "cnic-ssl-test2.com"}
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
        "DOMAIN": "cnic-ssl-test1.com",
        "FIRST": "0",
        "LAST": "1",
        "LIMIT": "2",
        "TOTAL": "4",
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

    # #.isPending
    # [in api response]
    r = R(rtm.getTemplate("pendingRegistration").getPlain(),
          {"COMMAND": "AddDomain", "DOMAIN": "mydomain.se"})
    assert r.isPending() is True
