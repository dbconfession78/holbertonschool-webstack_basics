#!/usr/bin/python3
"""
Module 10-simple_delete
"""


def simple_delete(my_dict, key=""):
    """
    Description - deletes a key in a dictionary
    :param my_dict: dict to delete from
    :param key: key of dict element to delete
    """
    if my_dict:
        my_dict.pop(key, None)
        return my_dict
