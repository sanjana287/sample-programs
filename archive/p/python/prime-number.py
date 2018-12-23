#!/usr/bin/env python
import sys
from math import sqrt, ceil


def is_prime(x):
    if x <= 1:
        return True
    if x % 2 == 0:
        return False
    return not bool([n for n in range(3, ceil(sqrt(x))+1) if x % n == 0])


def exit_with_error():
    print('Usage: please input a non-negative integer')
    sys.exit(1)


def main(args):
    try:
        x = int(args[0])
        if x < 0:
            exit_with_error()
        print(is_prime(x))
    except (IndexError,ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])
