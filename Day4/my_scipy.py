#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/12/2021
Purpose: Interpolation using Scipy and numpy
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


def get_data():
    ages = np.genfromtxt('ages.csv', delimiter=',', skip_header=1)
    # print(ages)
    years = ages[:, 0]  # full slice of first element
    print(years)
    males = ages[:, 1]  # full slice of second element
    print(males)
    # print(type(males))
    # Here years and males are values to approximate some function: males = f(years)
    f = interp1d(years, males)
    new_years = [1896, 1907, 1923, 1929,
                 1933, 1939, 1947, 1953,
                 1969, 1989, 1996, 1998]
    new_males = f(new_years)
    print(new_males)
    plt.plot(years, males, '-', new_years, new_males, 'o')
    plt.show()


# --------------------------------------------------
def main():
    """Make your noise here"""
    get_data()


# --------------------------------------------------
if __name__ == '__main__':
    main()
