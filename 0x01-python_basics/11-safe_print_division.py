#!/usr/bin/python3
"""
Module 11-safe_print_division
"""


def safe_print_division(a, b):
    """
    Description - divides two integers and prinst the result
    :param a: number being divided
    :param b: number doing the dividing
    """
    retval = None
    try:
        retval = a / b
    except:
        return
    finally:
        print("Inside result: {}".format(retval))
    return retval
