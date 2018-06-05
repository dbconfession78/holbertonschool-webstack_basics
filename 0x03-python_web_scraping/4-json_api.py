#!/usr/bin/python3
"""
Module 4-json_api
"""
import requests
from sys import argv


def main():
    url = "http://0.0.0.0:5000/search_user"
    letter = ""
    if len(argv) >= 2:
        letter = argv[1]
    payload = {"q": letter}
    r = requests.post(url, data=payload)
    content = r.json()
    if type(content) is dict:
        if content == {}:
            print("No result")
        else:
            print("[{}] {}".format(content.get("id"), content.get("name")))
    else:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
