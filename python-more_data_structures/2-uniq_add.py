#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    unique_integers = set(my_list)
    sum_unique = sum(unique_integers)
    return sum_unique
