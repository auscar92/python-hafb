#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""
from random import randrange


# --------------------------------------------------
def main():
    """Make your noise here"""
    # Random number between 0-99
    number = randrange(100)
    while True:
        guess = int(input('Guess a number:'))
        if guess == number:
            print('You got it')
            break


# --------------------------------------------------
if __name__ == '__main__':
    main()
