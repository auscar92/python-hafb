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


# --------------------------------------------------
if __name__ == '__main__':
    main()