#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

from math import sqrt
from pprint import pprint as pp

def is_prime(x):
    """
    Returns true or false if input is a prime number
    :param x: integer
    :return: True or False
    """
    if x < 2:
        return False
    for i in range (2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# --------------------------------------------------
def main():
    """Iterables and Comprehensions"""
    words = "Today I am very happy because Barcelona does not have Messi with them any more".split()
    print(words)
    lwords = []
    for word in words:
        lwords.append(len(word))
    print(lwords)
    # List Comprehension: [expr for item in iterable]
    totals = [len(word) for word in words]
    print(totals)
    # Add a predicate to your comprehension
    prime_nums = [x for x in range(1001) if is_prime(x)]
    print(prime_nums)
    print(f'The sum of the values {sum(prime_nums)}')
    print(f'You have {len(prime_nums)} in the first {len(range(1000))}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
