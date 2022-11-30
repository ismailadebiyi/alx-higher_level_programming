#!/usr/bin/python3
def uppercase(str):
    cvt = ''
    for c in str:
        if ord(c) >= 97:
            cvt += chr(ord(c) - 32)
        else:
            cvt += c
    print("{}".format(cvt))
