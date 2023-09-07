#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = argv[1:]
    if arguments:
        print("{} arguments:".format(len(arguments)))
    else:
        print("{} arguments.".format(len(arguments)))
    i = 1
    for arg in arguments:
        print("{:d}: {}".format(i, arg))
        i += 1
