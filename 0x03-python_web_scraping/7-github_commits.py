#!/usr/bin/python3
"""
Module 7-github_commits - list 10 commits (from the most recent to oldest) of
                          the repository “rails” by the user “rails” using the
                          Github API.
                          (https://developer.github.com/v3/repos/commits/)
"""


def main():
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    j = r.json()
    if j == []:
        print("No result")
    else:
        for i in range(10):
            elem = j[i]
            sha = elem.get('sha')
            author = elem.get('commit').get('author').get('name')
            item = "{} {}".format(sha, author)
            print(item)

if __name__ == "__main__":
    main()
