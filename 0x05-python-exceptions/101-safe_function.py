#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        print(f"Exception: {err}", file=sys.stderr)
        result = None
    return result

