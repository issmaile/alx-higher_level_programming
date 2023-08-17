#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ndir = a_dictionary.copy()
    keys_list = list(ndir.keys())

    for i in keys_list:
        ndir[i] *= 2

    return ndir
