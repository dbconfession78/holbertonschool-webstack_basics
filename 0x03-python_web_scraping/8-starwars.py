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
    r = requests.get(url)
    j = r.json()
    retval = []
    if type(j) is dict:
        if j == {}:
            print("No result")
        else:
            print("Number of results: {}".format(j.get("count")))
            while j.get('results'):
                results = j.get('results')
                for result in results:
                    retval.append(result.get("name"))
                if j.get("next"):
                    r = requests.get(j["next"])
                    j = r.json()
                else:
                    j = {}
            for elem in retval:
                print(elem)
    else:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
