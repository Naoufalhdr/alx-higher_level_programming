#!/usr/bin/python3
"""
Uses the GitHub API to display a GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth_header = {"Authorization": f"Basic {argv[1]}:{argv[2]}"}

    response = requests.get(url, headers=auth_header)
    print(response.json().get("id"))
