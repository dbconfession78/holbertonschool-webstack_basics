#!/usr/bin/python3
"""
Module 1-hbtn_header
"""
import requests
from sys import argv


def main():
    url = argv[1]
    email = argv[2]
    payload = {"email": email}
    r = requests.post(url, payload)
    print(r.content.decode("utf-8"))

if __name__ == "__main__":
    main()
