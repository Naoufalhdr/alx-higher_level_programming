#!/usr/bin/env bash
# Send a request to the URL and displays the size of the response body in bytes.
curl -s "$1" | wc -c
