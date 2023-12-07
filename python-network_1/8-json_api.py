#!/usr/bin/python3
"""
Module to send a POST request to http://0.0.0.0:5000/search_user with a letter
as a parameter.
Displays the result according to specified conditions.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    payload = {'q': letter}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()

        data = response.json()

        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
