#!/usr/bin/env python3
"""
Author: Austin Carey
Purpose: Say Hello to Waldo
"""

import argparse


def get_args():
    """
    Get the command-line arguments
    :return: list of parsed arguments
    """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """
    This is where the action is
    :return: Void
    """
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
