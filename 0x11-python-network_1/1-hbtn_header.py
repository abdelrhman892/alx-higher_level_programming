#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    rq = urllib.request.Request(argv[1])
    with urllib.request.urlopen(rq) as rspns:
        print(rspns.getheader('X-Request-Id'))
