#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    # Check if the number of arguments is not 4
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operators = {'+': add, '-': sub, '*': mul, '/': div}
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    # Check if the operator is valid and perform the operation
    if operator in operators:
        result = operators[operator](a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    else:
        print("Unknown operator. Available operators: +, -, *, and /")

