#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""
from pprint import pprint as pp


# --------------------------------------------------
def main():
    """Review Dictionaries"""
    urls = {'Google':"http://google.con",
            'Twitter': 'http://twitter.com',
            'WSU': 'http://weber.edu'}
    print(type(urls))
    print(urls)
    #curls = urls.copy()
    urls['WSU'] = 'http://weber.edu.tmp'
    print(urls)
    urls['yahoo'] = 'http://yahoo.com'
    print(urls)
    # to iterate over keys
    for key in urls:
        print(f'{key} => {urls[key]}')
    # to iterate over values
    for value in urls.values():
        print(f'values => {value}')
    # to iterate over both keys and values
    for key, value in urls.items():
        print(f'{key} => {value}')

    pp(urls)


# --------------------------------------------------
if __name__ == '__main__':
    main()
