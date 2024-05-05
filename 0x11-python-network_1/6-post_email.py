#!/usr/bin/python3
"""
Script to
- accepts a url and email
- send a POST request to the url
- display the response
"""

import requests
import sys


def send_request(url, email):
    try:
        data = {'email': email}
        response = requests.post(url, data=data)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response_body = send_request(url, email)
    print(response_body)
