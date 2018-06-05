#!/usr/bin/python3
"""
Module 1-hbtn_header
"""
import requests
from sys import argv


def main():
    url = argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))

if __name__ == "__main__":
    main()
