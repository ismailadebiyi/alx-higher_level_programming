#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nsum = 0
    for i in range(1, len(sys.argv)):
        nsum += int(sys.argv[i])
    print("{}".format(nsum))
