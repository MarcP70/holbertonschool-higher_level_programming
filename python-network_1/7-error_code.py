#!/usr/bin/python3
"""
Module to send a request to a URL and display the body of the response.
Prints an error message if the HTTP status code is greater than or equal
to 400.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        # Raises HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
