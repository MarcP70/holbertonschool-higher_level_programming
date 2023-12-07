#!/usr/bin/python3
"""
Module to use GitHub API with Basic Authentication and display user id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    try:
        response.raise_for_status()
        data = response.json()
        print(data.get('id'))
    except requests.exceptions.HTTPError:
        print("None")
