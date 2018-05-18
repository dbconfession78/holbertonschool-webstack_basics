#!/usr/bin/python3
"""
Module 1-print_comb2: prints 00 to 99
"""
for i in range(100):
    if i < 99:
        print('0{}'.format(i) if i < 10 else '{}'.format(i), end=", ")
    else:
        print("{}".format(i))
