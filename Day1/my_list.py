#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/9/2021
Purpose: Practice with Lists
"""


# --------------------------------------------------
def main():
    """Review lists"""
    r = [4, -2, 10, -18, 22, 2, 77]
    # Slicing
    print(r[2:6])
    print(f'len of list{len(r)} ')
    print(f'Last element {r[-1]}')
    # Copy list, by default Python uses shallow copies
    t = r
    print(f'1) Is t the same as r? {t is r}')
    # To make a copy, generate a new list
    u = r[:]
    print(f'2) Is u the same as r? {u is r}')
    v = r.copy() # faster
    print(f'2) Is v the same as r? {v is r}')
    print(f'2) Is v equivalent to r? {v == r}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
