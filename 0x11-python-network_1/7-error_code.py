#!/usr/bin/python3
"""
Script to
- accepts a url
- send a request to the url
- display the body of the response
"""

import requests
import sys


def fetch_urlbody(url):
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_urlbody(url)
