#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    print(f"Inside result: {result}")
    return result
