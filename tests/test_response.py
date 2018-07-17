from hexonet.apiconnector import connect
from hexonet.apiconnector.response import Response


def test_response():
    api = connect(
        "test.user",
        # wrong password
        "test.password",
        "https://coreapi.1api.net/api/call.cgi",
        "1234"
    )
    response = api.call({
        "COMMAND": "GetUserIndex"
    })
    assert isinstance(response, Response)
    assert response.description() == "Authentication failed"
    assert response.code() == 530
    assert isinstance(response.as_string(), str)
    assert isinstance(response.as_list_hash(), dict)
    assert isinstance(response.as_list(), list)
    assert len(response) == 0
    assert response["CODE"] == 530
    assert response.is_success() == False


def test_listresponse():
    api = connect(
        "test.user",
        "test.passw0rd",
        "https://coreapi.1api.net/api/call.cgi",
        "1234"
    )
    response = api.call({
        "COMMAND": "QueryDomainList",
        "VERSION": 2,
        "NOTOTAL": 1,  # TOTAL to have value from total to equal to count
        "LIMIT": 10,
        "FIRST": 0
    })
    assert isinstance(response, Response)
    assert response.description() == "Command completed successfully"
    assert response.code() == 200
    assert len(response) == 10
    assert isinstance(response[0], dict)
    assert isinstance(response.runtime(), float)
    assert isinstance(response.queuetime(), float)
    assert isinstance(response.properties(), dict)
    assert response.property("DOMAIN") is None
    assert isinstance(response.property("OBJECTID"), list)
    assert isinstance(response.property(), dict)
    assert response.property() == response.properties()
    assert response.is_success()
    assert response.is_tmp_error() == False
    assert isinstance(response.columns(), list)
    assert isinstance(response.first(), int)
    assert response.first() == 0
    assert isinstance(response.last(), int)
    assert response.last() == 9
    assert isinstance(response.count(), int)
    assert response.count() == 10
    assert isinstance(response.limit(), int)
    assert response.limit() == 10
    assert isinstance(response.total(), int)
    assert response.total() == 10
    assert isinstance(response.pages(), float)  # TODO int makes more sense
    assert response.pages() == 1.9  # doesn't make sense, should be 1 in this case
    assert isinstance(response.page(), int)
    assert response.page() == 1
    assert response.prevpage() is None
    assert response.prevpagefirst() is None
    assert response.nextpage() is None
    assert response.nextpagefirst() is None
    assert isinstance(response.lastpagefirst(), float)
    assert response.lastpagefirst() == 9.0

    Response(response.as_hash())
    # to cover isinstance dict check branch

    response = Response(
        b"[RESPONSE]\r\nCODE=421\r\nDESCRIPTION=Command failed due to server error. Client should try again\r\nEOF\r\n")
    assert response.is_tmp_error()
