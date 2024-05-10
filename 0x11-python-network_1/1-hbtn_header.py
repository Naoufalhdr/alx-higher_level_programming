#!/usr/bin/python3
""" Fetches the header value 'X-Request-id' of the specified URL and displays
it. """
from sys import argv
from urllib import request


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        html = response.info()
        print(html.get("X-Request-Id"))
