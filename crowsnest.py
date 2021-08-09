#!/usr/bin/env python3
"""
Author : t25 <auscar92@gmail.com>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    word = args.word
    article = ''
    if word == 'octopus':
        article = 'an'
    print(f'Ahoy, Captain, {article} {word} off the starboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
