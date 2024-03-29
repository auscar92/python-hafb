#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/9/2021
Purpose: Review tuples
"""

def minmax(items):
    """
    Return the maximum and minimum of the collection
    :param items: collection of objects
    :return: min and max
    """
    return min(items), max(items)


# --------------------------------------------------
def main():
    """Make your noise here"""

    # A tuple of any kind of object
    t = ("Ogden", 1.99, 2, 265e10) # paranthesis are optional
    print(t) # whole tuple
    print(type(t)) # type of object
    print(t[0]) # positional object
    print(f'Tuble is {len(t)} items long')
    # iterate over tuple
    for item in t:
        print(f'Item: {item}')

    t2 = t * 3
    for item in t2:
        print(f'Item: {item}')

    # Nested tuples
    a = ((1, 2), (10, 20), (100, 200))
    print(a[0][1])
    for l1 in a:
        for l2 in l1:
            print(f'Item 2 {l2}')


# --------------------------------------------------
if __name__ == '__main__':
    # main()
    items = (3, 88, 11, 22, 90)
    lower, upper = minmax(items)
    print(f'minimum {lower} and maximum {upper}')
    # Test for membership: in, not in
    if 3 in items:
        print("I have a 3")

    if 99 not in items:
        print("I do not have 99")