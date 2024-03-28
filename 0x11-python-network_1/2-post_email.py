#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    URL = argv[1]
    val = {'email': argv[2]}

    metaData = urllib.parse.urlencode(val)
    metaData = metaData.encode('ascii')
    rq = urllib.request.Request(URL, metaData)
    with urllib.request.urlopen(rq) as response:
        print(response.read().decode())
