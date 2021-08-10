#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/10/2021
Purpose:Review basics of classes
"""


class Point:
    pass


# --------------------------------------------------
def main():
    """Make your noise here"""
    p1 = Point()
    p2 = Point()
    # <object>.<attribute> = <value>
    p1.x = 5
    p1.y = 4
    p2.x = 3
    p2.y = 9
    print(p1.x, p1.y)
    print(p2.x, p2.y)


# --------------------------------------------------
if __name__ == '__main__':
    main()
