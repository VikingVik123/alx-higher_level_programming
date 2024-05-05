#!/usr/bin/python3
"""
Script to
- send a POST request
- check for conditions
- return a response
"""

import requests
import sys


def search_url(q=""):
    try:
        data = {'q': q}
        response = requests.post("http://0.0.0.0:5000/search_user", data=data)
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        search_url(sys.argv[1])
    else:
        search_url()
