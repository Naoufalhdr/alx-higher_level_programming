#!/usr/bin/python3
""" Fetches the content of the specified URL and prints the body of the
response."""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)
