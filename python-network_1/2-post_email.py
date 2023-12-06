#!/usr/bin/python3
"""
Module to send a POST request with an email parameter to a specified URL.
"""


import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print("Your email is:", body)
