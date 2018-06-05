#!/usr/bin/python3
"""
Module 5-starwars -  takes in a string and sends a search
                     request to the Star Wars API 'people' endpoint
                     (https://swapi.co/documentation)
"""


def main():
    import requests
    from sys import argv

    name = argv[1]
    url = "http://swapi.co/api/people/?search={}".format(name)
    r = requests.get(url)
    j = r.json()
    retval = []
    if type(j) is dict:
        if j == {}:
            print("No result")
        else:
            results = j.get('results')
            print("Number of result: {}".format(j.get("count")))
            for result in results:
                print(result.get("name"))
    else:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
