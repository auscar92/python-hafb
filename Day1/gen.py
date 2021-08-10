#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""


def take(count, iterable):
    """
    Take items from the front of the iterable
    :param count: The maximum number of items to retrieve
    :param iterable: The source series
    :yield: At most 'count' items for 'iterable
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(5, items):
        print(item)


def distinct(iterable):
    """
    Return unique items by eliminating duplicates
    :param iterable: The source series
    :yield: Unique elements in order from 'iterable'
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


def get_squares():
    squares = (num*num for num in range(1, 1001)) # Saves memory vs comprehension (with square brackets)
    print(type(squares))
    l_sq = list(squares)
    print(f'The sum of the first 1000 square numbers is: {sum(l_sq)}')


# --------------------------------------------------
def main():
    """Make your noise here"""
    #run_distinct()
    #run_pipeline()
    # Task: Create a list of the first 1 million square numbers
    get_squares()


# --------------------------------------------------
if __name__ == '__main__':
    main()
