#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as rspn:
    htmlFile = rspn.read()
print('Body response:')
print("\t- type: {}".format(type(htmlFile)))
print("\t- content: {}".format(htmlFile))
print("\t- utf8 content: {}".format(htmlFile.decode('utf-8')))
