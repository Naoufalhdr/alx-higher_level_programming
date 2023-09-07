#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    arguments = argv[:]

    # Check if the number of arguments is not 4
    if len(arguments) != 4:
        print("Usage: {} <a> <operator> <b>".format(arguments[0]))
        exit(1)

    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    # Check if the operator is valid and perform the operation
    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)
