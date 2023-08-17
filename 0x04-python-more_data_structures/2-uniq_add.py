#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    sm = 0
    for num in uniq_list:
        sm += num
    return sm
