#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""


# --------------------------------------------------
def main():
    """Make your noise here"""

    # List Comprehensions: [expr(item) for item in iterable]
    # Set Comprehensions: {expr[item for item in iterable}
    s = {i for i in range(10)}
    print(s)
    # Dict Comprehensions: {key_expr: value_expr for item in iterable}
    d = {i: i*2 for i in range(10)}
    print(d)
    # Comprehensions: (item for item in iterable)
    g = (i for i in range(10))
    print(g)

    # Multiple If-clauses
    points = []
    for x in range(5):
        for y in range(x):
            points.append((x,y))
    print(points)
    # Now use a comprehension
    points = [(x, y) for x in range(5) for y in range(3)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
