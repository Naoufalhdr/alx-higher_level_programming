#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = argv[1:]
    argc = len(arguments)
    delim = 's:' if argc > 1 else 's.' if argc == 0 else ':'
    print("{} argument{}".format(argc, delim))
    for i, arg in enumerate(arguments, 1):
        print("{:d}: {}".format(i, arg))
