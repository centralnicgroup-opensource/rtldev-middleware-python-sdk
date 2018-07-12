#!/usr/bin/python

# Import the ispapi library
import hexonet.apiconnector

# Create a connection with the URL, entity, login and password
# Use "1234" as entity for the OT&E, and "54cd" for productive use
# Don't have a HEXONET Account yet? Get one here: www.hexonet.net/sign-up
api = hexonet.apiconnector.connect(
    url='https://coreapi.1api.net/api/call.cgi',
    entity='1234',
    login='test.user',
    password='test.passw0rd'
)

# Call a command
response = api.call({
    'Command': "QueryDomainList", 'limit': 5
})

# Get the result in the format you want
rlist = response.as_list()
rhash = response.as_hash()
rlisthash = response.as_list_hash()

# Get the response code and the response description
code = response.code()
description = response.description()
