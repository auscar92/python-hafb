#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/10/2021
Purpose: Sorted Set Class
"""


class SortedSet:
    def __init__(self, items={}):
        """
        Create a sorted list , regardless of which iterable object you pass
        :param items: list of items
        """
        self._items = sorted(items)


# --------------------------------------------------
def main():
    """Make your noise here"""
    pass


# --------------------------------------------------
if __name__ == '__main__':
    main()
