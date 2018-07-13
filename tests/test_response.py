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
    assert type(response.as_string()) is str
    assert type(response.as_list_hash()) is dict
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
        "NOTOTAL": 1,#TOTAL to have value from total to equal to count
        "LIMIT": 10,
        "FIRST": 0
    })
    assert isinstance(response, Response)
    assert response.description() == "Command completed successfully"
    assert response.code() == 200
    assert len(response) == 10
    assert type(response[0]) is dict
    assert type(response.runtime()) is float
    assert type(response.queuetime()) is float
    assert type(response.properties()) is dict
    assert response.property("DOMAIN") is None
    assert isinstance(response.property("OBJECTID"), list)
    assert type(response.property()) is dict
    assert response.property() == response.properties()
    assert response.is_success() == True
    assert response.is_tmp_error() == False
    assert isinstance(response.columns(), list)
    assert type(response.first()) is int
    assert response.first() == 0
    assert type(response.last()) is int
    assert response.last() == 9
    assert type(response.count()) is int
    assert response.count() == 10
    assert type(response.limit()) is int
    assert response.limit() == 10
    assert type(response.total()) is int
    assert response.total() == 10
    assert type(response.pages()) is float #TODO int makes more sense
    assert response.pages() == 1.9 # doesn't make sense, should be 1 in this case
    assert type(response.page()) is int
    assert response.page() == 1
    assert response.prevpage() == None
    assert response.prevpagefirst() == None
    assert response.nextpage() == None
    assert response.nextpagefirst() == None
    assert type(response.lastpagefirst()) is float
    assert response.lastpagefirst() == 9.0