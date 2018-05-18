#!/usr/bin/python3
"""
Module 9-print_sorted_dictionary
"""


def print_sorted_dictionary(my_dict):
    """
    Description - prints a dict by ordered keys
    :param my_dict: dict to delete from
    """
    if my_dict is None:
        return

    for k, v in sorted(my_dict.items()):
        print("{}: {}".format(k, v))
