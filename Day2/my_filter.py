#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/10/2021
Purpose: Review the filter() function
"""


# --------------------------------------------------
def main():
    """Make your noise here"""
    numbers = [2, 5, 8, -1, 90, -2, -33, 12]
    # Task: Create a list of all positive numbers
    # List comprehension
    pos_nums = [x for x in numbers if x >= 0]
    print(pos_nums)
    # Generator
    positives = list((num for num in numbers if num >= 0))
    print(positives)
    # filter() and lambda
    positives = list(filter(lambda x: x >= 0, numbers))
    print(positives)


# --------------------------------------------------
if __name__ == '__main__':
    main()
