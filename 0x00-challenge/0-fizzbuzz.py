#!/usr/bin/python3
""" FizzBuzz Program
"""
import sys


def fizzbuzz(n):
    """
    This function prints numbers from 1 to n, each separated by a space.

    - For numbers divisible by three, it prints "Fizz" instead.
    - For numbers divisible by five, it prints "Buzz" instead.
    - For numbers divisible by both three and five, it prints "FizzBuzz".
    """
    if n < 1:
        return

    result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            result.append("FizzBuzz")
        elif (i % 3) == 0:
            result.append("Fizz")
        elif (i % 5) == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    print(" ".join(result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Number missing")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)
