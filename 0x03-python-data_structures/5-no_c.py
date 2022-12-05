#!/usr/bin/python3
def no_c(my_string):
    n_string = ""
    for c in my_string:
        if c != "c":
            if c != "C":
                n_string += c
    return n_string
