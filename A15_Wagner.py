#!/usr/bin/env python 118
# Matthew Graham Wagner
# Professor Coyle
# CSE 3342: Programming Languages
# 2 November 2017

#IMPORT libraries
import cgi
import json
import sys
import cgitb
import re

cgitb.enable()
#Tell Client what to expect either text/json or text/html
print "Content-Type: text/json\n"

#create a Python dictionary to send as JSON
mydict = {"test": True}

#extract paramters (keys and values) from client
parmObj = cgi.FieldStorage()

#iterate over keys - add key-value to mydict
for key in parmObj.keys():
    mydict[key] = parmObj.getvalue(key)

# convert dict to json string
json_data = json.dumps(mydict)

# send the JSON back to the client
print json_data