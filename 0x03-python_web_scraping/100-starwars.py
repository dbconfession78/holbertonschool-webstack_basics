#!/usr/bin/python3
"""
Module 100-starwars - takes in a string and sends a search
                      request to the Star Wars API 'people' endpoint
                      (https://swapi.co/documentation)
"""


def main():
    import requests
    from sys import argv

    def output(name, films):
        print(name)
        for film in films:
            print("\t{}".format(film))

    def get_films(urls):
        return [requests.get(url).json().get("title") for url in urls]

    param1 = argv[1]
    next = "http://swapi.co/api/people/?search={}".format(param1)
    while next:
        j = requests.get(next).json()
        if j.get("previous") is None:
            print("Number of result: {}".format(j.get("count")))
        for elem in j.get('results'):
            output(elem.get('name'), get_films(elem.get('films')))
        next = j["next"] if "next" in j else ""

if __name__ == "__main__":
    main()
