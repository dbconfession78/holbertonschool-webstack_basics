#!/usr/bin/env python3

if __name__ == "__main__":
    from sys import argv
    count = len(argv)-1
    if count == 0:
        print("0 arguments.")
    else:
        print("{} argument".format(count), end="s\n" if count != 1 else ":\n")
        for i in range(1, count+1):
            arg = argv[i]
            print("{:d}: {:s}".format(i, arg))
