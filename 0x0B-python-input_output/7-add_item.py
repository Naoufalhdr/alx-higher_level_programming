#!/usr/bin/python3
import json
from sys import argv
save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file

# Check if the file exists and load it's contents
try:
    items = load_json("add_item.json")
except FileNotFoundError:
    items = []

# Add command-line arguments to the list
for arg in argv[1:]:
    items.append(arg)

# Save the updated list to the file
save_json(items, "add_item.json")
