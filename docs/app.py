#!/usr/bin/python

# Import the ispapi library
from hexonet.apiconnector.apiclient import APIClient as AC

# -------- SESSIONLESS COMMUNICATION -----------

# Create a connection using the APIClient class and the appropriate
# methods to configure the connection as necessary.
# Don't have a HEXONET Account yet? Get one here:
# - Live System Account: https://www.hexonet.net/sign-up
# - Test/OT&E System Account: https://www.hexonet.net/signup-ote

cl = AC()
cl.useOTESystem()
cl.setCredentials('test.user', 'test.passw0rd')

# Call a command
r = cl.request({
    'Command': "QueryDomainList", 'limit': 5
})

# Get the result in the format you want
rlist = r.getListHash()
rhash = r.getHash()
rplain = r.getPlain()

# Get the response code and the response description
code = r.getCode()
description = r.getDescription()

# -------- SESSION-BASED COMMUNICATION -----------

cl = AC()
cl.useOTESystem()
cl.setCredentials('test.user', 'test.passw0rd')

# Call a command
r = cl.login()
# cl.login('12345678'); -> 2FA: one time password

if (r.isSuccess()):
    print("LOGIN SUCCEEDED!")
    r = cl.request({
        'Command': "QueryDomainList", 'limit': 5
    })
    rplain = r.getPlain()
    # ... further commands ...
    r = cl.logout()
    if (r.isSuccess()):
        print("LOGOUT SUCCEEDED!")

    
