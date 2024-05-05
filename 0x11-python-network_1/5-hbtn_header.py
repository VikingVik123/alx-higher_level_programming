#!/usr/bin/python3
"""
Script to
- fetch a url
- send a request to the url
- display the value
"""

import requests
import sys


def fetch_request_id(url):
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        return x_request_id
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    url = sys.argv[1]
    x_request_id = fetch_request_id(url)
    print(x_request_id)
