#!/usr/bin/python3
# Script to return the url response header
"""
script to
- take in a URL,
- send a request to the URL and display the value
"""

import sys
import urllib.request

def fetch_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            request_id = response.headers.get('X-Request-Id')
            if request_id:
                return request_id.strip()
            else:
                return "X-Request-Id not found in the response header."
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    request_id = fetch_request_id(url)
    print(request_id)
