#!/usr/bin/python3
""" Fetches the header value 'X-Request-id' of the specified URL and displays
it. """
from sys import argv
from urllib import request


with request.urlopen(argv[1]) as response:
    html = response.info()
    print(html["X-Request-Id"])
