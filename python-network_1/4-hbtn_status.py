#!/usr/bin/python3
"""
Module to fetch https://intranet.hbtn.io/status using the requests package
"""


import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
