#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_nums = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed_nums += 1
        except IndexError:
            break
    print("")
    return (printed_nums)
