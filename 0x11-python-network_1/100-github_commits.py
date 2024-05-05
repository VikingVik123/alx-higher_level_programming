#!/usr/bin/python3
"""
Script to
- Accept 2 arguments
- Gets for commits
- Returns the last 10
"""

import requests
import sys


def fetch_commits(repo_name, owner_name):
    try:
        url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
        response = requests.get(url)
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    fetch_commits(repo_name, owner_name)
