#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    olist = list(a_dictionary.keys())
    olist.sort()
    for i in olist:
        print("{}: {}".format(i, a_dictionary.get(i)))
