#!/usr/bin/python3
def number_keys(a_dictionary):
    keys_count = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        keys_count += 1

    return keys_count
