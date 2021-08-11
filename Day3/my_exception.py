#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""
from random import randrange


def more_info():
    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(e)
        print(f'encoding: {e.encoding}')
        print(f'reason: {e.reason}')
        print(f'object: {e.object}')
        print(f'start: {e.start}')
        print(f'end: {e.end}')


def median(iterable):
    """
    Obtain the center value of a series
    Sort the iterable and return the middle value if there is an odd
    number of elements, or the arithmetic mean of the middle two elements
    if there is an even number of elements
    :param iterable: a series of iterable items
    :exception ValueError for empty sequence
    :return: the median value
    """
    if len(iterable) == 0:
        raise ValueError('median() arg is an empty sequence')

    iterable.sort()
    half = (len(iterable)-1) // 2
    if len(iterable) % 2 == 0:
        return (iterable[half] + iterable[half+1]) / 2.0
    else:
        return iterable[half]


def test_median():
    # print(f'Median odd= {median([5, 2, 1, 4, 3])}')
    # print(f'Median even= {median([5, 2, 1, 4, 3, 6])}')
    # print(f'Median even= {median([])}')
    try:
        median([])
    except ValueError as e:
        print(f'Payload: {e.args}')
        print(f'{str(e)}')



def lookups():
    s = [1, 4, 6]
    try:
        item = s[5]
    #except IndexError: # Is a subclass of LookupError
    except LookupError: # first
        print('Handled IndexError')

    d = dict(a=65, b=33)
    try:
        value = d['x']
    # except KeyError: # is a subclass of LookupError
    except LookupError: # first
        print('Handled KeyError')


# --------------------------------------------------
def main():
    """Make your noise here"""
    # Random number between 0-99
    number = randrange(10)
    while True:
        try:
            guess = int(input('Guess a number:'))
        except ValueError:
            continue
        if guess == number:
            print('You got it')
            break


# --------------------------------------------------
if __name__ == '__main__':
    #main()
    #lookups()
    #test_median()
    more_info()
