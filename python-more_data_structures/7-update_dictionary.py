#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None or key is None or value is None:
        return
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
