#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/12/2021
Purpose: Practice basics of Numpy: https://numpy.org/
"""
import numpy as np


def np_arrays():
    array_one = np.array([1, 2, 3, 4])
    print(array_one, type(array_one))
    numbers = [9, 7, 10, 12]
    print(numbers, type(numbers))
    array_two = np.array(numbers)
    print(array_two, type(array_two))
    # Create arrays with initial placeholders
    # array_of_zeros = np.zeros((3, 4))
    # print(array_of_zeros)
    # array_of_ones = np.ones((3, 4))
    # print(array_of_ones)
    # array_of_empty = np.empty((3, 4))
    # print(array_of_empty)
    # Eye indexing a matrix
    array_eye = np.eye(3)
    print(array_eye)
    # Ranges with numpy
    array_of_events = np.arange(2, 20, 2)
    print(array_of_events)
    array_of_events = np.arange(0, 2, 0.3)  # including floats
    print(array_of_events)
    # N-dimensional arrays, reshape an array
    array_nd = np.arange(6).reshape(3, 2) # Only take arguments that multiply to the arange input value
    print(array_nd)


def np_print_arrays():
    c = np.arange(24).reshape(2, 3, 4)
    print(c)
    # "Pretty" print
    print(np.arange(10000).reshape(100, 100))


def np_arithmetic_operations():
    a = np.array([10, 10, 10])
    b = np.array([5, 5, 5])
    # Simple operations
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a % 3)
    print(a < 20)
    print(a ** 2)
    # Dot function
    A = np.array([[1, 1], [0, 1]])  # 2D [[]]
    B = np.array([[2,0], [3, 4]])
    print(f'A:{A}')
    print(f'B:{B}')
    print(f'Multiplication: {A*B}')
    print(f'Dot: {A.dot(B)}')
    print(a)
    a *= 3
    print(a)
    # Unary operators
    ages = np.array([12, 15, 18, 20])
    print(f'Sum: {ages.sum()}')
    print(f'Min: {ages.min()}')
    print(f'Max: {ages.max()}')


# --------------------------------------------------
def main():
    """Make your noise here"""
    # np_arrays()
    # np_print_arrays()
    np_arithmetic_operations()


# --------------------------------------------------
if __name__ == '__main__':
    main()
