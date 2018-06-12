#!/usr/bin/python3
"""
Module 8-starwars -  takes in a string and sends a search
                     request to the Star Wars API 'people' endpoint
                     (https://swapi.co/documentation)
"""


def main():
    import requests
    from sys import argv

    name = argv[1]
    url = "http://swapi.co/api/people/?search={}".format(name)
    retval = []
    while url:
        r = requests.get(url)
        j = r.json()
        results = j.get('results')
        for result in results:
            retval.append(result.get("name"))
            url = j.get("next")
    print("Number of results: {}".format(j.get("count")))
    for elem in retval:
        print(elem)


if __name__ == "__main__":
    main()
