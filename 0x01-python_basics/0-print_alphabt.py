#!/usr/bin/python3
letter = 97

for i in range(0, 26):
    if chr(letter) != "q" and chr(letter) != "e":
        print("{}".format(chr(letter)), end='')
    letter = letter + 1
