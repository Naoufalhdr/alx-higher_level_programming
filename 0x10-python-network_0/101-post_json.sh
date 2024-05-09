#!/bin/bash
# Send POST request with data stored in a JSON file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
