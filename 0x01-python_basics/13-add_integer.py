#!/usr/bin/python3
"""
Module 13-add_integer
"""


def add_integer(a, b):
    """
    Description - adds 2 integers
    :param a: first integer in addition
    :param b: second integer in addition
    """
    type_set = {int, float}
    if type(a) not in type_set:
        raise TypeError("a must be an integer")
    if type(b) not in type_set:
        raise TypeError("b must be an integer")
    return int(a + b)
