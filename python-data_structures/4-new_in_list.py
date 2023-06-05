#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        if idx in range(len(my_list)):
            new_list = my_list[:]
            new_list[idx] = element
            return new_list
    return my_list[:]
