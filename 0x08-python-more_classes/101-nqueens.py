#!/usr/bin/python3
import sys


def main():
    """main function"""

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if number < 4:
        print("N must be at least 4")
        sys.exit(1)

    print(number)

if __name__ == "__main__":
    main()
