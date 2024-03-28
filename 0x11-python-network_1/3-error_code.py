#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as rsp:
            print(rsp.read().decode())
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
