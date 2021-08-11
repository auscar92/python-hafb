#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/11/2021
Purpose: Discuss callable objects, callable instances, and lambdas
"""
import socket
from pprint import pp


# def resolve(host):
#     return socket.gethostbyname(host)


class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache


def test_resolver():
    # print(resolve) # functions are callable objects (First class citizens)
    # print(resolve('weber.edu'))
    # print(resolve('google.com'))
    resolve = Resolver()
    print(resolve('weber.edu'))
    print(resolve('google.com'))
    print(resolve.has_host('weber.edu'))
    resolve.clear()
    print(resolve('google.com'))
    print(resolve.__call__('yahoo.com'))
    # Call the class itself
    print(Resolver)
    # call the instance
    print(resolve)


def sequence_class(immutable):
    # if immutable:
    #     cls = tuple
    # else:
    #     cls = list
    # return cls
    return tuple if immutable else list


def test_sequence_class():
    seq = sequence_class(immutable=True)
    t = seq('Ogden')
    print(t)
    print(type(t))
    seq = sequence_class(immutable=False)
    t = seq('Ogden')
    print(t)
    print(type(t))


def test_lambda():
    scientist = ['Marie Curie',
                 'Albert Einstein',
                 'Niel Bohr',
                 'Dimitri Mendeleev',
                 'Charles Darwin',
                 'Isaac Newton']
    # Call built-in sorted() with a lambda def
    pp(sorted(scientist, key=lambda name:name.split()[-1]))


def last_name(name):
    return name.split()[-1]


# --------------------------------------------------
def main():
    """Make your noise here"""
    # test_Resolver
    #test_sequence_class()
    test_lambda()


# --------------------------------------------------
if __name__ == '__main__':
    main()
