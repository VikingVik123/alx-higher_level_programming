#!/usr/bin/python3
"""
Script to
- fetch a url
- print a response
"""

import requests


def fetch_status(url):
    try:
        response = requests.get(url)
        body = {
            "type": str(type(response.text)),
            "content": response.text
        }
        return body
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    status = fetch_status(url)
    print("Body response:")
    for key, value in status.items():
        print(f"\t- {key}: {value}")
