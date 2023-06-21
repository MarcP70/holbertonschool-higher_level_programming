#!/usr/bin/python3
"""
This script adds command line arguments to a list stored in a JSON file.
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    filename = "add_item.json"
    my_list = load_from_json_file(filename) + sys.argv[1:]
except Exception:
    my_list = sys.argv[1:]
finally:
    save_to_json_file(my_list, filename)
