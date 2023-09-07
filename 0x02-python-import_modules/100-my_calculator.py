#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    operators = {'+': add, '-': sub, '*': mul, '/': div}
    a, operator, b = int(argv[1]), argv[2], int(argv[3])
    if operator in operators:
        result = operators[operator](a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
