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


def import_data_pandas(data):
    # load data from csv files
    data = pd.read_csv('countries.csv')
    print(data.head())
    print(f'Total of {len(set(data.country))} unique countries')
    # Plot data from one country
    afghanistan = data[data.country == 'Afghanistan']
    plt.plot(afghanistan.year, afghanistan.gdpPerCapita)
    plt.title("Afghanistan's GDP Per Capita")
    plt.show()


def continent_data(data):
    # Compare Asia and Europe's GDP per capita
    # Get the list of continents
    continents = set(data.continent)
    print(continents)
    data_2007 = data[data.year == 2007]
    asia_2007 = data_2007[data_2007.continent == 'Asia']
    europe_2007 = data_2007[data_2007.continent == 'Europe']
    # Print number of countries per continent
    print(f'Asia countries: {len(set(asia_2007.country))}')
    print(f'Europe countries: {len(set(europe_2007.country))}')
    # Get mean and median
    print(f'Mean GDP in Asia {asia_2007.gdpPerCapita.mean()}')
    print(f'Median GDP in Asia {asia_2007.gdpPerCapita.median()}')
    print(f'Mean GDP in Europe {europe_2007.gdpPerCapita.mean()}')
    print(f'Median GDP in Europe {europe_2007.gdpPerCapita.median()}')
    # make subplots
    plt.subplot(2, 1, 1)
    plt.title('Distribution of GDP Per Capita')
    plt.hist(asia_2007.gdpPerCapita, 20, range=(0, 50000), edgecolor='black')
    plt.ylabel('Asia')
    plt.subplot(2, 1, 2)
    plt.hist(europe_2007.gdpPerCapita, 20, range=(0, 50000), edgecolor='black')
    plt.ylabel('Europe')
    plt.show()


def continent_data_le(data):
    """Compare the life expectancy distribution between
    Europe and America in 1997"""
    continents = set(data.continent)
    data_1997 = data[data.year == 1997]
    americas_1997 = data_1997[data_1997.continent == 'Americas']
    europe_1997 = data_1997[data_1997.continent == 'Europe']
    # make subplots
    bins = 20
    plt.subplot(211)
    plt.title('Distribution of Life Expectancy')
    plt.hist(americas_1997.lifeExpectancy, bins, range=(55, 85), edgecolor='black')
    plt.ylabel('Americas')
    plt.subplot(212)
    plt.hist(europe_1997.lifeExpectancy, bins, range=(55, 88), edgecolor='black')
    plt.ylabel('Europe')
    plt.show()


def continent_data_gdp_growth(data):
    usa = data[data.country == 'United States']
    china = data[data.country == 'China']
    # Calculate growth
    usa_growth = usa.gdpPerCapita / (usa.gdpPerCapita.iloc[0]*100)
    china_growth = china.gdpPerCapita / (china.gdpPerCapita.iloc[0]*100)

    plt.title('GDP per Capita Growth(first year = 100)')
    plt.plot(usa.year, usa_growth)
    plt.plot(china.year, china_growth)
    plt.legend(['United States', 'China'])
    plt.xlabel('Year')
    plt.ylabel('GDP per capita growth')
    plt.show()


# --------------------------------------------------
def main():
    """Make your noise here"""
    data = pd.read_csv('countries.csv')
    #import_data_pandas(data)
    #continent_data(data)
    #continent_data_le(data)
    continent_data_gdp_growth(data)


# --------------------------------------------------
if __name__ == '__main__':
    main()
