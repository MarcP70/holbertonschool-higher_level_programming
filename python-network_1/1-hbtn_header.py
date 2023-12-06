#!/usr/bin/python3
"""
Module to send a request to a URL and display the value of the X-Request-Id
variable in the header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header_value = response.getheader('X-Request-Id')
        print(header_value)
