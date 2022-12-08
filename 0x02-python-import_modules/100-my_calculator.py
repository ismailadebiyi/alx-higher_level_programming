#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv[1:]) != 3:
        print("{}, Usage:{} <a> <operator> <b>".format(len(argv[1:]), argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    math = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in math:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, operator, b, math[operator](a, b)))
