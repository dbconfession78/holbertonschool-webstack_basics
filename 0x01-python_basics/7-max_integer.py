#!/usr/bin/python3
"""
Module 7-max_integer
"""


def max_integer(my_list=[]):
    """
    Description - returns the highest integer in an input list.
    :param my_list: the list to find the highest integer in.
    """
    if not my_list:
        return None
    return sorted(my_list)[-1]
