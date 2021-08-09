#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""




# --------------------------------------------------
def main():
    """Review ranges"""
    r = range(5)
    print(r)
    print(type(r))
    for item in r:
        print(item)
    print("break")
    # Set the upper and lower limit
    r = range(5, 10)
    for item in r:
        print(item)
    # Create list out of ranges
    l = list(range(5, 10))
    print(l)
    print(type(l))
    for item in r:
        print(item)

# --------------------------------------------------
if __name__ == '__main__':
    main()
