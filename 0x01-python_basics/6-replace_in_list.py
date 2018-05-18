#!/usr/bin/python3
"""
Module 6-replace_in_list
"""


def replace_in_list(my_list, idx, element):
    """
    Description - replaces the value at a specified index in a list
    :param my_list: the list in question
    :param idx: the idx to replace value at
    :param element: the value to repalce at the given index
    """
    if idx < len(my_list) and idx >= 0:
        my_list[idx] = element
    return my_list
