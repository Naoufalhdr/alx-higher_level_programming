#!/usr/bin/python3
""" sends a request to the URL and displays the value of the variable
X-Request-Id """
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print(r.headers.get("X-Request-Id"))
