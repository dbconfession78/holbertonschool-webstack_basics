#!/usr/bin/python3
"""
Module 2-is_lower
"""


def islower(c):
    """
    Description - determines if a charcter is lowercase.
    :param c: the character to check for lowercase.
    """
    return ord(c) in range(97, 123)
