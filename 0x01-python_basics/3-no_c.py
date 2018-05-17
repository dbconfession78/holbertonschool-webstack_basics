#!/usr/bin/env python3
def no_c(str):
    while True:
        x = str.lower().find('c')
        if x == -1:
            break
        str = str[0:x] + str[x+1:]
    return str
