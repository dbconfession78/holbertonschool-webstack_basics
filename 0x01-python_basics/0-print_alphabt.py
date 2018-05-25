#!/usr/bin/python3
"""
Module 0-print_alphabt
"""
for i in range(97, 123):
    if chr(i) not in {'q', 'e'}:
        print("{}".format(chr(i)), end='')
