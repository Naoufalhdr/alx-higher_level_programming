#!/usr/bin/python3
""" Fetches the content of the specified URL and prints the body of the
response."""
from urllib import request


with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html = response.read()
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('utf-8'))
