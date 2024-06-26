#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response. """
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    status = r.status_code
    if (status >= 400):
        print("Error code:", status)
    else:
        print(r.text)
