#!/usr/bin/python3
"""
Module 6-my_github -  takes a Github credential (username and password) and
                      uses the Github API to display ther id
"""


def main():
    import requests
    from sys import argv

    if len(argv) != 3:
        print("Please provide username and password.")
        quit()

    username = argv[1]
    pw = argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(username, pw))
    j = r.json()
    if type(j) is dict:
        if j == {}:
            print("No result")
        else:
            if j.get('id'):
                print(j['id'])
            else:
                print(None)
    else:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
