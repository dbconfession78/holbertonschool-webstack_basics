#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""


def main():
    """ Entry point """
    import requests
    from sys import argv

    query = argv[1]
    next = 'https://swapi.co/api/people/?search={}'.format(query)
    names = []
    while (next):
        json = requests.get(next).json()
        results = json.get('results')
        for result in results:
            names.append(result['name'])

        try:
            next = json['next']
        except:
            next = None

    print('Number of results: {}'.format(json.get('count')))
    for name in names:
        print(name)

if __name__ == '__main__':
    main()
