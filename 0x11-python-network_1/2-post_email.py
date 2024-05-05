#!/usr/bin/python3
# Script to fetch the mail address
"""
script to
- take in a URL
- take email as a parameter
- display the body of the response
"""

import urllib.parse
import urllib.request
import sys

def fetch_email(url, email):
    try:
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')

        request = urllib.request.Request(url, data=data, method='POST')
        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            return body
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response_body = fetch_email(url, email)
    print(response_body)
