from centralnicreseller.apiconnector.apiclient import (
    APIClient as AC,
    CNR_CONNECTION_URL_LIVE,
    CNR_CONNECTION_URL_PROXY,
)
from centralnicreseller.apiconnector.response import Response as R
from centralnicreseller.apiconnector.responsetemplatemanager import (
    ResponseTemplateManager as RTM,
)
import pytest
import platform
import os
import urllib.parse

rtm = RTM()


def test_apiclientmethods():
    cl = AC()
    rtm.addTemplate(
        "login200",
        "[RESPONSE]\r\nproperty[expiration date][0]=2024-09-19 10:52:51\r\nproperty[sessionid][0]=bb7a884b09b9a674fb4a22211758ce87\r\ndescription=Command completed successfully\r\ncode=200\r\nqueuetime=0.004\r\nruntime=0.023\r\nEOF\r\n",
    )
    rtm.addTemplate("login500", rtm.generateTemplate("530", "Authentication failed"))
    rtm.addTemplate("OK", rtm.generateTemplate("200", "Command completed successfully"))
    rtm.addTemplate(
        "listP0",
        "[RESPONSE]\r\nproperty[total][0]=4\r\nproperty[first][0]=0\r\nproperty[domain][0]=cnic-ssl-test1.com\r\nproperty[domain][1]=cnic-ssl-test2.com\r\nproperty[count][0]=2\r\nproperty[last][0]=1\r\nproperty[limit][0]=2\r\ndescription=Command completed successfully\r\ncode=200\r\nqueuetime=0\r\nruntime=0.007\r\nEOF\r\n",
    )
    rtm.addTemplate(
        "listP1",
        "[RESPONSE]\r\nproperty[total][0]=4\r\nproperty[first][0]=2\r\nproperty[domain][0]=emailcustomization.com\r\nproperty[domain][1]=test-keysysbe0123.be\r\nproperty[count][0]=2\r\nproperty[last][0]=3\r\nproperty[limit][0]=2\r\ndescription=Command completed successfully\r\ncode=200\r\nqueuetime=0\r\nruntime=0.006\r\nEOF\r\n",
    )
    rtm.addTemplate(
        "listFP0",
        "[RESPONSE]\r\nproperty[total][0]=4\r\nproperty[first][0]=0\r\nproperty[domain][0]=cnic-ssl-test1.com\r\nproperty[count][0]=1\r\nproperty[last][0]=0\r\nproperty[limit][0]=1\r\ndescription=Command completed successfully\r\ncode=200\r\nqueuetime=0\r\nruntime=0.009\r\nEOF\r\n",
    )
    rtm.addTemplate(
        "listFP1",
        "[RESPONSE]\r\nproperty[total][0]=4\r\nproperty[first][0]=1\r\nproperty[domain][0]=cnic-ssl-test2.com\r\nproperty[count][0]=1\r\nproperty[last][0]=1\r\nproperty[limit][0]=1\r\ndescription=Command completed successfully\r\ncode=200\r\nqueuetime=0\r\nruntime=0.007\r\nEOF\r\n",
    )
    rtm.addTemplate(
        "listFP2",
        "[RESPONSE]\r\nproperty[total][0]=4\r\nproperty[first][0]=2\r\nproperty[domain][0]=emailcustomization.com\r\nproperty[count][0]=1\r\nproperty[last][0]=2\r\nproperty[limit][0]=1\r\ndescription=Command completed successfully\r\ncode=200\r\nqueuetime=0\r\nruntime=0.007\r\nEOF\r\n",
    )
    # #.getPOSTData()
    # test object input with special chars
    validate = "s_command=AUTH%3Dgwrgwqg%25" + "%26%5C44t3%2A%0ACOMMAND%3DModifyDomain"
    enc = cl.getPOSTData({"COMMAND": "ModifyDomain", "AUTH": "gwrgwqg%&\\44t3*"})
    assert enc == validate

    # test string input
    enc = cl.getPOSTData("gregergege")
    assert enc == "s_command=gregergege"

    # test object input with null value in parameter
    validate = "s_command=COMMAND%3DModifyDomain"
    enc = cl.getPOSTData({"COMMAND": "ModifyDomain", "AUTH": None})
    assert enc == validate

    # test secured passwords
    cl.setCredentials(
        os.environ.get("CNR_TEST_USER"), os.environ.get("CNR_TEST_PASSWORD")
    )
    cl.enableDebugMode()
    enc = cl.getPOSTData(
        {
            "COMMAND": "CheckAuthentication",
            "SUBUSER": os.environ.get("CNR_TEST_USER"),
            "PASSWORD": os.environ.get("CNR_TEST_PASSWORD"),
        },
        True,
    )
    cl.setCredentials("", "")

    cnr_test_user = os.environ.get("CNR_TEST_USER")
    encoded_user = urllib.parse.quote(cnr_test_user.encode()) if cnr_test_user else ""

    expected = (
        "s_login="
        + encoded_user
        + "&s_pw=***&"
        + "s_command=COMMAND%3DCheckAuthentication%0APASSWORD%3D%2A%2A%2A%0ASUBUSER%3D"
        + encoded_user
    )
    assert expected == enc

    # #.enableDebugMode()
    cl.enableDebugMode()
    cl.disableDebugMode()

    # #.getURL()
    assert cl.getURL() == CNR_CONNECTION_URL_LIVE

    # #.getUserAgent()
    pid = "PYTHON-SDK"
    pyv = platform.python_version()
    pf = platform.system()
    arch = platform.architecture()[0]
    ua = "%s (%s; %s; rv:%s) python/%s" % (pid, pf, arch, cl.getVersion(), pyv)
    assert cl.getUserAgent() == ua

    # #.setUserAgent()
    pid = "WHMCS"
    rv = "7.7.0"
    pid2 = "python-sdk"
    pyv = platform.python_version()
    pf = platform.system()
    arch = platform.architecture()[0]
    ua = "%s (%s; %s; rv:%s) %s/%s python/%s" % (
        pid,
        pf,
        arch,
        rv,
        pid2,
        cl.getVersion(),
        pyv,
    )
    cl2 = cl.setUserAgent(pid, rv)
    assert isinstance(cl2, AC) is True
    assert cl.getUserAgent() == ua

    mods = ["reg/2.6.2", "ssl/7.2.2", "dc/8.2.2"]
    ua = "%s (%s; %s; rv:%s) %s %s/%s python/%s" % (
        pid,
        pf,
        arch,
        rv,
        " ".join(mods),
        pid2,
        cl.getVersion(),
        pyv,
    )
    cl2 = cl.setUserAgent(pid, rv, mods)
    assert isinstance(cl2, AC) is True
    assert cl.getUserAgent() == ua

    # #.setURL()
    tmp = CNR_CONNECTION_URL_PROXY
    url = cl.setURL(tmp).getURL()
    assert url is tmp
    cl.setURL(CNR_CONNECTION_URL_LIVE)

    # [credentials and session set]
    sessionobj = {
        "socketcfg": {
            "login": "myaccountid",
            "session": "12345678",
        }
    }
    cl.setCredentials("myaccountid", "mypassword")
    cl.reuseSession(sessionobj)
    cl.enableDebugMode()
    tmp = cl.getPOSTData({"COMMAND": "StatusAccount"})
    exp = "s_login=myaccountid&s_sessionid=12345678&s_command=COMMAND%3DStatusAccount"
    assert tmp == exp

    # [session and login reset]
    cl.reuseSession({})
    cl.setCredentials("", "")
    tmp = cl.getPOSTData({"COMMAND": "StatusAccount"})
    assert tmp == "s_command=COMMAND%3DStatusAccount"

    # #.saveSession/reuseSession with password
    sessionobj = {}
    cl.useOTESystem()
    cl.setCredentials(
        os.environ.get("CNR_TEST_USER"), os.environ.get("CNR_TEST_PASSWORD")
    ).disableDebugMode()
    r = cl.login()
    cl.saveSession(sessionobj)
    cl2 = AC()
    cl2.reuseSession(sessionobj)
    tmp = cl2.getPOSTData({"COMMAND": "StatusAccount"})
    assert "s_sessionid" in tmp

    # #.setCredentials()
    # [credentials set]
    cl.setCredentials("myaccountid", "mypassword")
    tmp = cl.getPOSTData({"COMMAND": "StatusAccount"})
    exp = "s_login=myaccountid&s_pw=mypassword&s_command=COMMAND%3DStatusAccount"
    assert tmp == exp

    # [session reset]
    cl.setCredentials("", "")
    tmp = cl.getPOSTData({"COMMAND": "StatusAccount"})
    assert tmp == "s_command=COMMAND%3DStatusAccount"

    # #.setRoleCredentials()
    # [role credentials set]
    cl.setRoleCredentials("myaccountid", "myroleid", "mypassword")
    tmp = cl.getPOSTData({"COMMAND": "StatusAccount"})
    exp = "s_login=myaccountid%3Amyroleid&s_pw=mypassword&s_command=COMMAND%3DStatusAccount"
    assert tmp == exp

    # [role credentials reset]
    cl.setRoleCredentials("", "", "")
    tmp = cl.getPOSTData({"COMMAND": "StatusAccount"})
    assert tmp == "s_command=COMMAND%3DStatusAccount"

    # #.login()
    # [login succeeded; no role used]
    cl.useOTESystem()
    cl.setCredentials(
        os.environ.get("CNR_TEST_USER"), os.environ.get("CNR_TEST_PASSWORD")
    )
    r = cl.login()
    assert isinstance(r, R) is True
    assert r.isSuccess() is True, ("{0} {1}").format(r.getCode(), r.getDescription())
    rec = r.getRecord(0)
    assert rec is not None
    assert rec.getDataByKey("SESSIONID") is not None

    # support bulk parameters also as nested array (flattenCommand)
    cl.enableDebugMode()
    r = cl.request(
        {"COMMAND": "CheckDomains", "DOMAIN": ["example.com", "example.net"]}
    )
    assert isinstance(r, R) is True
    cmd = r.getCommand()
    keys = cmd.keys()
    assert ("DOMAIN0" in keys) is True
    assert ("DOMAIN1" in keys) is True
    assert ("DOMAIN" in keys) is False
    assert cmd["DOMAIN0"] == "example.com"
    assert cmd["DOMAIN1"] == "example.net"

    # support autoIDNConvert
    r = cl.request(
        {
            "COMMAND": "CheckDomains",
            "DOMAIN": "GOOGLE.COM",
            "DNSZONE": ["example.com", "dömäin.com", "example.net"],
        }
    )
    assert isinstance(r, R) is True
    cmd = r.getCommand()
    keys = cmd.keys()
    assert ("DNSZONE0" in keys) is True
    assert ("DNSZONE1" in keys) is True
    assert ("DNSZONE2" in keys) is True
    assert ("DNSZONE" in keys) is False
    assert cmd["DNSZONE0"] == "example.com"
    assert cmd["DNSZONE1"] == "xn--dmin-moa0i.com"
    assert cmd["DNSZONE2"] == "example.net"

    # [login succeeded]
    cl.useOTESystem()
    cl.setCredentials(
        os.environ.get("CNR_TEST_USER"), os.environ.get("CNR_TEST_PASSWORD")
    )
    r = cl.login()
    assert isinstance(r, R)
    assert r.isSuccess() is True, ("{0} {1}").format(r.getCode(), r.getDescription())
    rec = r.getRecord(0)
    assert rec is not None
    assert rec.getDataByKey("SESSIONID") is not None

    # [login failed; wrong credentials]
    cl.setCredentials(os.environ.get("CNR_TEST_USER"), "WRONGPASSWORD")
    r = cl.login()
    assert isinstance(r, R)
    assert r.isError() is True

    # [login failed; http error]
    tpl = rtm.getTemplate("httperror")
    old = cl.getURL()
    cl.setURL("https://iwontsucceedgregegeg343teagr43.com/api/call.cgi")
    cl.setCredentials(os.environ.get("CNR_TEST_USER"), "WRONGPASSWORD")
    r = cl.login()
    assert isinstance(r, R)
    assert r.isTmpError() is True
    assert r.getDescription() == tpl.getDescription()
    cl.setURL(old)

    # [login succeeded; no session returned]
    # TODO: need network mock
    tpl = R(rtm.getTemplate("OK").getPlain())
    cl.useOTESystem()
    cl.setCredentials(
        os.environ.get("CNR_TEST_USER"), os.environ.get("CNR_TEST_PASSWORD")
    )
    r = cl.login()
    assert isinstance(r, R)
    assert r.isSuccess() is True

    # # #.logout()
    # # [logout succeeded]
    r = cl.logout()
    assert isinstance(r, R)
    assert r.isSuccess() is True

    # # [logout failed; session no longer exists]
    tpl = R(rtm.getTemplate("login200").getPlain())
    cl.enableDebugMode()
    sessionobj = {
        "socketcfg": {
            "login": os.environ.get("CNR_TEST_USER"),
            "session": tpl.getRecord(0).getDataByKey("SESSIONID"),
        }
    }
    cl.reuseSession({})
    r = cl.logout()
    assert isinstance(r, R) is True
    assert r.isError() is True

    # #.request()
    # [200 < r.statusCode > 299]
    # TODO need network mock
    # tpl2 = R(rtm.getTemplate('httperror').getPlain())
    # cl.setCredentials(os.environ.get("CNR_TEST_USER"), os.environ.get("CNR_TEST_PASSWORD"))
    # cl.useOTESystem()
    # r = cl.request({ 'COMMAND': 'StatusAccount' })
    # assert isinstance(r, R) is True
    # assert r.isTmpError() is True
    # assert r.getCode() == tpl2.getCode()
    # assert r.getDescription() == tpl2.getDescription()

    # [200 < r.statusCode > 299, no debug]
    # TODO need network mock
    # tpl2 = R(rtm.getTemplate('httperror').getPlain())
    # cl.disableDebugMode()
    # r = cl.request({ 'COMMAND': 'GetUserIndex' })
    # assert isinstance(r, R)
    # assert r.isTmpError() is True
    # assert r.getCode() == tpl2.getCode()
    # assert r.getDescription() == tpl2.getDescription()

    # .requestNextResponsePage
    # [no LAST set]
    cl.setCredentials(
        os.environ.get("CNR_TEST_USER"), os.environ.get("CNR_TEST_PASSWORD")
    )
    cl.useOTESystem()
    cl.enableDebugMode()
    r = R(
        rtm.getTemplate("listP0").getPlain(),
        {"COMMAND": "QueryDomainList", "LIMIT": 2},
    )
    nr = cl.requestNextResponsePage(r)
    assert r.isSuccess() is True
    assert nr.isSuccess() is True
    assert r.getRecordsLimitation() == 2
    assert nr.getRecordsLimitation() == 2
    assert r.getRecordsCount() == 2
    assert nr.getRecordsCount() == 2
    assert r.getFirstRecordIndex() == 0
    assert r.getLastRecordIndex() == 1
    assert nr.getFirstRecordIndex() == 2
    assert nr.getLastRecordIndex() == 3

    # #.requestAllResponsePages()
    # [success case]
    nr = cl.requestAllResponsePages({"COMMAND": "QueryDomainList"})
    assert len(nr) > 0

    # #.setUserView()
    cl.setUserView("julia")
    r = cl.request({"COMMAND": "QueryUserList"})
    assert isinstance(r, R) is True
    assert r.isSuccess() is True

    # #.resetUserView()
    cl.setUserView("julia")
    cl.resetUserView()
    r = cl.request({"COMMAND": "QueryUserList"})
    assert isinstance(r, R) is True
    assert r.isSuccess() is True

    # #.setProxy
    cl.setProxy("https://127.0.0.1:8080")
    assert cl.getProxy() == "https://127.0.0.1:8080"
    cl.setProxy("")

    # #.setReferer
    cl.setReferer("https://www.centralnicreseller.com/")
    assert cl.getReferer() == "https://www.centralnicreseller.com/"
    cl.setReferer("")

    # #.useHighPerformanceConnectionSetup
    cl.useHighPerformanceConnectionSetup()
    assert cl.getURL() == CNR_CONNECTION_URL_PROXY

    # #.useDefaultConnectionSetup
    cl.useDefaultConnectionSetup()
    assert cl.getURL() == CNR_CONNECTION_URL_LIVE
