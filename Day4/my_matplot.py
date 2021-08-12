#!/usr/bin/env python3
"""
Author : t25 <me@wsu.com>
Date   : 8/12/2021
Purpose: Test matplotlib, numpy, and pandas
"""
from matplotlib import pyplot as plt
import pandas as pd


def first_matplotlib():
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.xlabel('This the x axis')
    plt.ylabel('This the y axis')
    plt.title('My first plot')
    plt.show()


def first_pandas():
    data = {'year': [2008, 2012, 2016],
            'attendees': [112, 321, 729],
            'average age': [24, 43, 31]}
    df = pd.DataFrame(data)
    print(df)
    # Get one col
    print(df['year'])
    print(type(df['year']))
    earlier_than_2013 = df['year'] < 2013
    # print(df['earlier_than_2013'])
    # print(earlier_than_2013)
    plt.plot(df['year'], df['attendees'])
    plt.plot(df['year'], df['average age'])
    plt.legend(['attendees', 'average age'])
    plt.show()


# --------------------------------------------------
def main():
    """Make your noise here"""
    first_pandas()


# --------------------------------------------------
if __name__ == '__main__':
    main()
