#!/usr/bin/python3
"""
Module 0-print_alphabt: prints a-z excluding q and e
"""
for i in range(97, 123):
    if chr(i) not in {'q', 'e'}:
        print(chr(i), end='')
