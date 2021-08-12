#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/12/2021
Purpose: Setup script for distribution of my super package
"""
from distutils.core import setup

setup(
    name='class_decorator',
    version='0.1',
    py_modules=['my_class_decorator'],
    # Metadata
    author='Waldo Weber',
    author_email='waldo@weber.edu',
    description='A module that shows how to use Class deorators',
    license='Public domain',
    keywords='decorators'
)