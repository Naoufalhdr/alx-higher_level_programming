#!/usr/bin/python3
"""  takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response """
from sys import argv
from urllib import request


if __name__ == "__main__":
    url = argv[1]
    email = argv[2].encode('utf-8')
    req = request.Request(url, data=email)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
