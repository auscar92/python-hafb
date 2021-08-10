#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/10/2021
Purpose: Review the map() function
"""


# --------------------------------------------------
def main():
    """Make your noise here"""
    # Map() is lazy. It only produces the values as they are needed
    m = map(ord, 'The purple Weber State')
    print(m)
    print(next(m)) # one at a time, "on demand"
    print(next(m))
    print(next(m))
    # print(list(m))
    print(list(map(ord, 'The purple Weber State')))


# --------------------------------------------------
if __name__ == '__main__':
    main()
