#!/usr/bin/env python
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
#mydict = {"Situation": "Valid", "PhoneNum": "936-647-6243", "State": "New York"}
#mydict = {"Situation": "InvalidFormat", "PhoneNum": "936-647-6242"}
mydict = {"Situation": "InvalidAreaCode", "AreaCode": "936"}


#extract paramters (keys and values) from client
areaObj = cgi.FieldStorage()
phoneNumObj = cgi.FieldStorage()
#iterate over keys - add key-value to mydict
for key in areaObj.keys():
    mydict[key] = areaObj.getvalue(key)

# convert dict to json string
json_data = json.dumps(mydict)

# send the JSON back to the client
print json_data