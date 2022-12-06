#!/usr/bin/python3
def max_integer(my_list=[]):
    max_v = 0
    if my_list == []:
        return "None"
    for i in my_list:
        if i > max_v:
            max_v = i
    return max_v
