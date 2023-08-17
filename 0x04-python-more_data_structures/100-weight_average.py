#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    summ = 0
    total_weights = 0

    for tup in my_list:
        summ += tup[0] * tup[1]
        total_weights += tup[1]

    return (summ/total_weights)
