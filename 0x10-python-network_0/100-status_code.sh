#!/bin/bash
# Send a request to that URL and display only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
