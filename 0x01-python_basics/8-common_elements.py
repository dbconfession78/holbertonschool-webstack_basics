#!/usr/bin/python3
"""
Module 8-common_elements
"""


def common_elements(set_1, set_2):
    """
    Description - returns a set of common elements in two sets
    :param set_1: first input set
    :param set_2: second input set
    """
    return {x for x in set_1 if x in set_2}
