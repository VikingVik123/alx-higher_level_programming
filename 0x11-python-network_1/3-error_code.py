#!/usr/bin/python3
"""
Script to
- accepts a url
- sends a request to the url
- displays the body of the response
"""

import urllib.request
import urllib.error
import sys


def fetch_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            return body
    except urllib.error.HTTPError as e:
        return f"Error code: {e.code}"


if __name__ == "__main__":
    url = sys.argv[1]
    response_body = fetch_url(url)
    print(response_body)
