from hexonet.apiconnector.apiclient import APIClient as AC, ISPAPI_CONNECTION_URL, ISPAPI_CONNECTION_URL_PROXY
from hexonet.apiconnector.response import Response as R
from hexonet.apiconnector.responsetemplatemanager import ResponseTemplateManager as RTM
import pytest
import platform

rtm = RTM()


def test_apiclientmethods():
    cl = AC()
    rtm.addTemplate(
        'login200',
        '[RESPONSE]\r\nPROPERTY[SESSION][0]=h8JLZZHdF2WgWWXlwbKWzEG3XrzoW4y' +
        'shhvtqyg0LCYiX55QnhgYX9cB0W4mlpbx\r\nDESCRIPTION=Command completed' +
        ' successfully\r\nCODE=200\r\nQUEUETIME=0\r\nRUNTIME=0.169\r\nEOF\r' +
        '\n'
    )
    rtm.addTemplate(
        'login500',
        rtm.generateTemplate('530', 'Authentication failed')
    )
    rtm.addTemplate(
        'OK',
        rtm.generateTemplate('200', 'Command completed successfully')
    )
    rtm.addTemplate(
        'listP0',
        '[RESPONSE]\r\nPROPERTY[TOTAL][0]=2701\r\nPROPERTY[FIRST][0]=0\r\nP' +
        'ROPERTY[DOMAIN][0]=0-60motorcycletimes.com\r\nPROPERTY[DOMAIN][1]=' +
        '0-be-s01-0.com\r\nPROPERTY[COUNT][0]=2\r\nPROPERTY[LAST][0]=1\r\nP' +
        'ROPERTY[LIMIT][0]=2\r\nDESCRIPTION=Command completed successfully' +
        '\r\nCODE=200\r\nQUEUETIME=0\r\nRUNTIME=0.023\r\nEOF\r\n'
    )
    rtm.addTemplate(
        'listP1',
        '[RESPONSE]\r\nPROPERTY[TOTAL][0]=2701\r\nPROPERTY[FIRST][0]=2\r\nP' +
        'ROPERTY[DOMAIN][0]=0-qas-ao17-0.org\r\nPROPERTY[DOMAIN][1]=0-sunny' +
        'da222y.com\r\nPROPERTY[COUNT][0]=2\r\nPROPERTY[LAST][0]=3\r\nPROPE' +
        'RTY[LIMIT][0]=2\r\nDESCRIPTION=Command completed successfully\r\nC' +
        'ODE=200\r\nQUEUETIME=0\r\nRUNTIME=0.032\r\nEOF\r\n'
    )
    rtm.addTemplate(
        'listFP0',
        '[RESPONSE]\r\nPROPERTY[TOTAL][0]=3\r\nPROPERTY[FIRST][0]=0\r\nPROP' +
        'ERTY[DOMAIN][0]=0-60motorcycletimes.com\r\nPROPERTY[COUNT][0]=1\r' +
        '\nPROPERTY[LAST][0]=1\r\nPROPERTY[LIMIT][0]=1\r\nDESCRIPTION=Comma' +
        'nd completed successfully\r\nCODE=200\r\nQUEUETIME=0\r\nRUNTIME=0.' +
        '023\r\nEOF\r\n'
    )
    rtm.addTemplate(
        'listFP1',
        '[RESPONSE]\r\nPROPERTY[TOTAL][0]=3\r\nPROPERTY[FIRST][0]=1\r\nPROP' +
        'ERTY[DOMAIN][0]=0-be-s01-0.com\r\nPROPERTY[COUNT][0]=1\r\nPROPERTY' +
        '[LAST][0]=2\r\nPROPERTY[LIMIT][0]=1\r\nDESCRIPTION=Command complet' +
        'ed successfully\r\nCODE=200\r\nQUEUETIME=0\r\nRUNTIME=0.032\r\nEOF' +
        '\r\n'
    )
    rtm.addTemplate(
        'listFP2',
        '[RESPONSE]\r\nPROPERTY[TOTAL][0]=3\r\nPROPERTY[FIRST][0]=2\r\nPROP' +
        'ERTY[DOMAIN][0]=0-qas-ao17-0.org\r\nPROPERTY[COUNT][0]=2\r\nPROPER' +
        'TY[LAST][0]=3\r\nPROPERTY[LIMIT][0]=1\r\nDESCRIPTION=Command compl' +
        'eted successfully\r\nCODE=200\r\nQUEUETIME=0\r\nRUNTIME=0.032\r\nE' +
        'OF\r\n'
    )

    # #.getPOSTData()
    # test object input with special chars
    validate = (
        's_entity=54cd&s_command=AUTH%3Dgwrgwqg%25' +
        '%26%5C44t3%2A%0ACOMMAND%3DModifyDomain'
    )
    enc = cl.getPOSTData({
        'COMMAND': 'ModifyDomain',
        'AUTH': 'gwrgwqg%&\\44t3*'
    })
    assert enc == validate

    # test string input
    enc = cl.getPOSTData('gregergege')
    assert enc == 's_entity=54cd&s_command=gregergege'

    # test object input with null value in parameter
    validate = 's_entity=54cd&s_command=COMMAND%3DModifyDomain'
    enc = cl.getPOSTData({
        "COMMAND": 'ModifyDomain',
        "AUTH": None
    })
    assert enc == validate

    # test secured passwords
    cl.setCredentials('test.user', 'test.passw0rd')
    enc = cl.getPOSTData({
        'COMMAND': 'CheckAuthentication',
        'SUBUSER': 'test.user',
        'PASSWORD': 'test.passw0rd'
    }, True)
    cl.setCredentials('', '')
    expected = (
        's_entity=54cd&s_login=test.user&s_pw=***&' +
        's_command=COMMAND%3DCheckAuthentication%0APASSWORD%3D%2A%2A%2A%0ASUBUSER%3Dtest.user'
    )
    assert expected == enc

    # #.enableDebugMode()
    cl.enableDebugMode()
    cl.disableDebugMode()

    # #.getSession()
    # initial value
    session = cl.getSession()
    assert session is None
    # custom value
    sessid = 'testSessionID12345678'
    cl.setSession(sessid)
    session = cl.getSession()
    assert session is sessid
    cl.setSession('')

    # #.getURL()
    assert cl.getURL() == ISPAPI_CONNECTION_URL

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
    ua = "%s (%s; %s; rv:%s) %s/%s python/%s" % (pid, pf, arch, rv, pid2, cl.getVersion(), pyv)
    cl2 = cl.setUserAgent(pid, rv)
    assert isinstance(cl2, AC) is True
    assert cl.getUserAgent() == ua

    mods = ["reg/2.6.2", "ssl/7.2.2", "dc/8.2.2"]
    ua = "%s (%s; %s; rv:%s) %s %s/%s python/%s" % (pid, pf, arch, rv, " ".join(mods), pid2, cl.getVersion(), pyv)
    cl2 = cl.setUserAgent(pid, rv, mods)
    assert isinstance(cl2, AC) is True
    assert cl.getUserAgent() == ua

    # #.setURL()
    tmp = ISPAPI_CONNECTION_URL_PROXY
    url = cl.setURL(tmp).getURL()
    assert url is tmp
    cl.setURL(ISPAPI_CONNECTION_URL)

    # #.setOTP()
    # [otp set]
    cl.setOTP('12345678')
    tmp = cl.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    exp = 's_entity=54cd&s_otp=12345678&s_command=COMMAND%3DStatusAccount'
    assert tmp == exp

    # [otp reset]
    cl.setOTP('')
    tmp = cl.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    exp = 's_entity=54cd&s_command=COMMAND%3DStatusAccount'
    assert tmp == exp

    # #.setSession()
    # [session set]
    cl.setSession('12345678')
    tmp = cl.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    exp = 's_entity=54cd&s_session=12345678&s_command=COMMAND%3DStatusAccount'
    assert tmp == exp

    # [credentials and session set]
    cl.setRoleCredentials('myaccountid', 'myrole', 'mypassword')
    cl.setOTP('12345678')
    cl.setSession('12345678')
    tmp = cl.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    exp = 's_entity=54cd&s_session=12345678&s_command=COMMAND%3DStatusAccount'
    assert tmp == exp

    # [session reset]
    cl.setSession('')
    tmp = cl.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    assert tmp == 's_entity=54cd&s_command=COMMAND%3DStatusAccount'

    # #.saveSession/reuseSession
    sessionobj = {}
    cl.setSession('12345678').saveSession(sessionobj)
    cl2 = AC()
    cl2.reuseSession(sessionobj)
    tmp = cl2.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    exp = 's_entity=54cd&s_session=12345678&s_command=COMMAND%3DStatusAccount'
    assert tmp == exp
    cl.setSession('')

    # #.setRemoteIPAddress()
    # [ip set]
    cl.setRemoteIPAddress('10.10.10.10')
    tmp = cl.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    exp = (
        's_entity=54cd&s_remoteaddr=10.10.10.10&s_command=COMMAND%3DStatusAccount'
    )
    assert tmp == exp

    # [ip reset]
    cl.setRemoteIPAddress('')
    tmp = cl.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    assert tmp == 's_entity=54cd&s_command=COMMAND%3DStatusAccount'

    # #.setCredentials()
    # [credentials set]
    cl.setCredentials('myaccountid', 'mypassword')
    tmp = cl.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    exp = (
        's_entity=54cd&s_login=myaccountid&s_pw=mypassword&s_command=COMMAND%3DStatusAccount'
    )
    assert tmp == exp

    # [session reset]
    cl.setCredentials('', '')
    tmp = cl.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    assert tmp == 's_entity=54cd&s_command=COMMAND%3DStatusAccount'

    # #.setRoleCredentials()
    # [role credentials set]
    cl.setRoleCredentials('myaccountid', 'myroleid', 'mypassword')
    tmp = cl.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    exp = (
        's_entity=54cd&s_login=myaccountid%21myroleid&s_pw=mypassword&s_command=COMMAND%3DStatusAccount'
    )
    assert tmp == exp

    # [role credentials reset]
    cl.setRoleCredentials('', '', '')
    tmp = cl.getPOSTData({
        'COMMAND': 'StatusAccount'
    })
    assert tmp == 's_entity=54cd&s_command=COMMAND%3DStatusAccount'

    # #.login()
    # [login succeeded; no role used]
    cl.useOTESystem()
    cl.setCredentials('test.user', 'test.passw0rd')
    cl.setRemoteIPAddress('1.2.3.4')
    r = cl.login()
    assert isinstance(r, R) is True
    assert r.isSuccess() is True, ("{0} {1}").format(r.getCode(), r.getDescription())
    rec = r.getRecord(0)
    assert rec is not None
    assert rec.getDataByKey('SESSION') is not None

    # support bulk parameters also as nested array (flattenCommand)
    r = cl.request({
        'COMMAND': 'CheckDomains',
        'DOMAIN': ['example.com', 'example.net']
    })
    assert isinstance(r, R) is True
    assert r.isSuccess() is True
    assert r.getCode() is 200
    assert r.getDescription() == "Command completed successfully"
    cmd = r.getCommand()
    keys = cmd.keys()
    assert ("DOMAIN0" in keys) is True
    assert ("DOMAIN1" in keys) is True
    assert ("DOMAIN" in keys) is False
    assert cmd["DOMAIN0"] == "example.com"
    assert cmd["DOMAIN1"] == "example.net"

    # support autoIDNConvert
    r = cl.request({
        'COMMAND': 'CheckDomains',
        'DOMAIN': ['example.com', 'dömäin.example', 'example.net']
    })
    assert isinstance(r, R) is True
    assert r.isSuccess() is True
    assert r.getCode() is 200
    assert r.getDescription() == "Command completed successfully"
    cmd = r.getCommand()
    keys = cmd.keys()
    assert ("DOMAIN0" in keys) is True
    assert ("DOMAIN1" in keys) is True
    assert ("DOMAIN2" in keys) is True
    assert ("DOMAIN" in keys) is False
    assert cmd["DOMAIN0"] == "example.com"
    assert cmd["DOMAIN1"] == "xn--dmin-moa0i.example"
    assert cmd["DOMAIN2"] == "example.net"

    # [login succeeded; role used]
    # cl.useOTESystem()
    #cl.setRoleCredentials('test.user', 'testrole', 'test.passw0rd')
    #r = cl.login()
    #assert isinstance(r, R)
    #assert r.isSuccess() is True, ("{0} {1}").format(r.getCode(), r.getDescription())
    #rec = r.getRecord(0)
    #assert rec is not None
    #assert rec.getDataByKey('SESSION') is not None

    # [login failed; wrong credentials]
    cl.setCredentials('test.user', 'WRONGPASSWORD')
    r = cl.login()
    assert isinstance(r, R)
    assert r.isError() is True

    # [login failed; http error]
    tpl = rtm.getTemplate('httperror')
    old = cl.getURL()
    cl.setURL('https://iwontsucceedgregegeg343teagr43.com/api/call.cgi')
    cl.setCredentials('test.user', 'WRONGPASSWORD')
    r = cl.login()
    assert isinstance(r, R)
    assert r.isTmpError() is True
    assert r.getDescription() == tpl.getDescription()
    cl.setURL(old)

    # [login succeeded; no session returned]
    # TODO: need network mock
    # tpl = R(rtm.getTemplate('OK').getPlain())
    # cl.useOTESystem()
    # cl.setCredentials('test.user', 'test.passw0rd')
    # r = cl.login()
    # assert isinstance(r, R)
    # assert r.isSuccess() is True
    # rec = r.getRecord(0)
    # assert rec is Node

    # #.loginExtended()
    # [login succeeded; no role used]
    cl.useOTESystem()
    cl.setCredentials('test.user', 'test.passw0rd')
    r = cl.loginExtended({
        'TIMEOUT': 60
    })
    assert isinstance(r, R) is True
    assert r.isSuccess() is True
    rec = r.getRecord(0)
    assert rec is not None
    assert rec.getDataByKey('SESSION') is not None

    # #.logout()
    # [logout succeeded]
    r = cl.logout()
    assert isinstance(r, R)
    assert r.isSuccess() is True

    # [logout failed; session no longer exists]
    tpl = R(rtm.getTemplate('login200').getPlain())
    cl.enableDebugMode()
    cl.setSession(tpl.getRecord(0).getDataByKey('SESSION'))
    r = cl.logout()
    assert isinstance(r, R) is True
    assert r.isError() is True

    # #.request()
    # [200 < r.statusCode > 299]
    # TODO need network mock
    # tpl2 = R(rtm.getTemplate('httperror').getPlain())
    # cl.setCredentials('test.user', 'test.passw0rd')
    # cl.useOTESystem()
    # r = cl.request({ 'COMMAND': 'GetUserIndex' })
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
    cl.setCredentials('test.user', 'test.passw0rd')
    cl.useOTESystem()
    r = R(
        rtm.getTemplate('listP0').getPlain(),
        {'COMMAND': 'QueryDomainList', 'LIMIT': 2, 'FIRST': 0}
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

    # [LAST set]
    r = R(rtm.getTemplate(
        'listP0').getPlain(),
        {'COMMAND': 'QueryDomainList', 'LIMIT': 2, 'FIRST': 0, 'LAST': 1}
    )
    with pytest.raises(
        Exception,
        match=r'Parameter LAST in use.'
    ):
        cl.requestNextResponsePage(r)

    # [no FIRST set]
    cl.disableDebugMode()
    r = R(
        rtm.getTemplate('listP0').getPlain(),
        {'COMMAND': 'QueryDomainList', 'LIMIT': 2}
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
    nr = cl.requestAllResponsePages(
        {'COMMAND': 'QuerySSLCertList', 'FIRST': 0, 'LIMIT': 100}
    )
    assert len(nr) > 0

    # #.setUserView()
    cl.setUserView('hexotestman.com')
    r = cl.request({'COMMAND': 'GetUserIndex'})
    assert isinstance(r, R) is True
    assert r.isSuccess() is True

    # #.resetUserView()
    cl.setUserView('')
    r = cl.request({'COMMAND': 'GetUserIndex'})
    assert isinstance(r, R) is True
    assert r.isSuccess() is True

    # #.setProxy
    cl.setProxy('https://127.0.0.1:8080')
    assert cl.getProxy() == 'https://127.0.0.1:8080'
    cl.setProxy('')

    # #.setReferer
    cl.setReferer('https://www.hexonet.net/')
    assert cl.getReferer() == 'https://www.hexonet.net/'
    cl.setReferer('')

    # #.useHighPerformanceConnectionSetup
    cl.useHighPerformanceConnectionSetup()
    assert cl.getURL() == ISPAPI_CONNECTION_URL_PROXY

    # #.useDefaultConnectionSetup
    cl.useDefaultConnectionSetup()
    assert cl.getURL() == ISPAPI_CONNECTION_URL
