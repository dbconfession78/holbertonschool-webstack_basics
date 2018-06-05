#!/usr/bin/python3
"""
Module 0-hbtn_status
"""
import requests


def main():
    r = requests.get("https://intranet.hbtn.io/status")
    content = r.content.decode("utf-8")
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

if __name__ == "__main__":
    main()
