#!/usr/bin/python3
"""
Module 1-hbtn_header
"""
import requests
from sys import argv


def main():
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.content.decode("utf-8"))


if __name__ == "__main__":
    main()
