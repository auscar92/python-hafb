#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/10/2021
Purpose: Sorted Set Class
"""


class SortedSet:
    def __init__(self, items=None):
        """
        Create a sorted list , regardless of which iterable object you pass
        :param items: list of items
        """
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        # print(index)
        # print(type(index))
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return 'SortedSet({})'.format(repr(self._items) if self._items else '')

    def __eq__(self, rhs):
        """If not instance return NoImplemented rather than raise NoImplementedError"""
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def __ne__(self, rhs):
        """If not instance return NoImplemented rather than raise NoImplementedError"""
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items


# --------------------------------------------------
def main():
    """Make your noise here"""
    pass


# --------------------------------------------------
if __name__ == '__main__':
    main()
