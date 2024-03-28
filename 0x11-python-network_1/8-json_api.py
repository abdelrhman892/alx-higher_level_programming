#!/usr/bin/python3
"""
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        Chr = ""
    else:
        Chr = argv[1]
    URL = 'http://0.0.0.0:5000/search_user'
    pay_load = {'q': Chr}
    req = requests.post(URL, data=pay_load)

    try:
        dict = req.json()
        if dict:
            print("[{}] {}".format(dict.get('id'), dict.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
