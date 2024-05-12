#!/usr/bin/python3
""" list 10 commits of the repository “rails” by the user “rails”
using the GitHub API"""
from sys import argv
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    headers = {"accept": "application/vnd.github+json"}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    for commit in json_data[:10]:
        sha = commit.get("sha")
        auth_name = commit.get("commit").get("author").get("name")

        print(f"{sha}: {auth_name}")
