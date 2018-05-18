#!/usr/bin/python3
"""
Module 3-no_c
"""


def no_c(str):
    """
    Description - removes all instances of 'c' and 'C' from a str
    :param str: the string to remove c's from
    """
    while True:
        x = str.lower().find('c')
        if x == -1:
            break
        str = str[0:x] + str[x+1:]
    return str
