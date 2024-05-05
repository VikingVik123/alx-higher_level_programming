#!/usr/bin/python3
"""
Script to
- get github id
- use authentication
- return
"""

import requests
import sys


def fetch_github_id(username, password):
    try:
        url = "https://api.github.com/user"
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            return response.json().get("id")
        else:
            return None
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    github_id = fetch_github_id(username, password)
    print(github_id)
