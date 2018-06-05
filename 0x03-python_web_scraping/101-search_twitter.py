#!/usr/bin/python3
"""
Module 101-search_twitter.py - sends a search request to the Twitter API
             (https://developer.twitter.com/en/docs/api-reference-index)
"""


def main():
    import twitter
    from sys import argv

    consumer_key = argv[1]
    consumer_secret = argv[2]
    search_string = argv[3]

    # consumer_key = "dDIXGhK8YqOK8XSkUhk7qC8QQ"
    # consumer_secret = "eWhzDaqtGP6NtJ4pMoLtxZnthd2J88WM9XPKxDhr5wwaGUnQkN"
    # search_string = "#holbertonschool"

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key="767413788882640897-6050iGwDYoL7V0rA1W4"
                      "sl44grNS4Wrl",
                      access_token_secret="hXduOK7aJXI5L5415qTrl0dVEI5YWXxlu9Y"
                      "7ntDjIicaN")

    ret = api.GetSearch(search_string)
    for i in range(5):
        elem = ret[i]
        j = elem._json
        _id = j.get("id")
        text = j.get("text")
        author = elem.user.name
        print("[{}] {} by {}".format(_id, text, author))

if __name__ == "__main__":
    main()
