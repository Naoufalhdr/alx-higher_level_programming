#!/usr/bin/python3
""" This script takes in a letter and sends a POST request to a URL with the
letter as a parameter. """
from sys import argv
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) >= 2:
        r = requests.get(url, data={'q': argv[1]})
        try:
            json_data = r.json()
            if json_data:
                print(f"[{json_data.get('id')}] {json_data.get('name')}")
            else:
                print("No result")
        except requests.exceptions.JSONDecodeError as json_err:
            print("Not a valid JSON")
    else:
        print("No result")
