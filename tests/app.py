#!/usr/bin/python

# Import the cnr library
from centralnicreseller.apiconnector.apiclient import APIClient as AC
import os

# -------- SESSIONLESS COMMUNICATION -----------

# Create a connection using the APIClient class and the appropriate
# methods to configure the connection as necessary.
print("---- SESSIONLESS COMMUNICATION ----")
cl = AC()
cl.useOTESystem()
cl.setCredentials(os.environ.get("CNR_TEST_USER"), os.environ.get("CNR_TEST_PASSWORD"))
# use the below method in case you have an active
# ip filter setting

# Call a command
r = cl.request({"Command": "QueryDomainList", "limit": 5})

# Get the result in the format you want
rlist = r.getListHash()
rhash = r.getHash()
rplain = r.getPlain()

# or use API methods to access specific data
col = r.getColumn("DOMAIN")  # get column domain
if col:
    col.getData()  # get all data of column DOMAIN
r.getColumnKeys()  # get all column keys
r.getColumnIndex("DOMAIN", 0)  # get data for column DOMAIN at index 0
r.getColumns()  # get all columns
r.getRecord(0)  # row at index 0
r.getRecords()  # get all rows
# ... and some more

# Get the response code and the response description
code = r.getCode()
description = r.getDescription()
print(str(code) + " " + description)

# -------- SESSION-BASED COMMUNICATION -----------
print("---- SESSION-BASED COMMUNICATION ----")
cl = AC()
cl.useOTESystem()
cl.setCredentials(os.environ.get("CNR_TEST_USER"), os.environ.get("CNR_TEST_PASSWORD"))

# Call a command
r = cl.login()

if r.isSuccess():
    print("LOGIN SUCCEEDED!")
    r = cl.request({"Command": "QueryDomainList", "limit": 5})
    rplain = r.getPlain()
    code = r.getCode()
    description = r.getDescription()
    print(str(code) + " " + description)
    # ... further commands ...
    r = cl.logout()
    if r.isSuccess():
        print("LOGOUT SUCCEEDED!")
