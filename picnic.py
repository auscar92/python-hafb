#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',  # Plus means one or more arguments
                        help='Item(s) to  bring on a picnic')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    item = list(args.item)
    print(item)

    if args.sorted:
        item.sort()

    # 1 Item, just print item
    # 2 Items: item1 and item2
    # 3 or more Items: item1, item2, itemx, and itemLast
    bringing = ' '
    if len(item) == 1:
        bringing = item[0]
    elif len(item) == 2:
        bringing = f'{item[0]} and {item[1]}'
    elif len(item) > 2:
        item[-1] = f'and {item[-1]}'
        bringing = ', '.join(item)


    # Print info
    print(f'You are bringing {bringing}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
