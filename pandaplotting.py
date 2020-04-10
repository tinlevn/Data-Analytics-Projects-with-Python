"""
By:
Jeremy Devore
Tin Le
"""
#Please chagne file path on your machine.
#Compilation time is long.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import math
from datetime import datetime

input_file1 = Path('D:\SP500.csv')
input_file2 = Path('D:\Sacramentorealestatetransactions.csv')

LINE_WIDTH = 60
NUM_GROUPS = 30
MAX_FIG_COLUMNS = 5

def main():
    """
    Part 1:
    real estate transaction .csv file
    """
    df2 = pd.read_csv(input_file2)

    """
    Question 1:
    Create a grid of scatter plots with each one representing the sq_ft 
    distribution in a single zipcode, please also include ticks, labels 
    and legend in your plot
    """
    df2['group_num'] = pd.cut(df2.index, bins=NUM_GROUPS,
                              labels=range(NUM_GROUPS))
    groupby_zip = df2.groupby(['zip'])
    num_zips = df2['zip'].nunique()
    fig, axes = plt.subplots(math.ceil(num_zips / MAX_FIG_COLUMNS),
                             MAX_FIG_COLUMNS, sharex=True, sharey=True)
    for ax, data in zip(axes.flatten(), groupby_zip):
        ax.scatter(data[1]['group_num'], data[1]['sq__ft'])
        ax.set_xlabel('Group Number')
        ax.set_ylabel('Square ft')
        ax.set_title(data[0])
        ax.legend('Properties')
        ax.set_xticks(range(NUM_GROUPS))

    """
    Question 2:
    Create a grid of scatter plots with each one representing the price 
    distribution in a single zipcode, annotate the highest and lowest 
    price ones for each category of real estate: condo, residential and 
    multi-family, please also include ticks, labels and legend in your 
    plot
    """

    fig, axes = plt.subplots(math.ceil(num_zips / MAX_FIG_COLUMNS),
                             MAX_FIG_COLUMNS, sharex=True, sharey=True)
    for ax, data in zip(axes.flatten(), groupby_zip):
        ax.scatter(data[1]['group_num'], data[1]['price'])
        ax.set_xlabel('Group Number')
        ax.set_ylabel('Price')
        ax.set_title(data[0])
        ax.legend('Properties')
        ax.set_xticks(range(NUM_GROUPS))

        groupby_type = data[1].groupby(['type'])
        for prop_type, prop_data in groupby_type:
            max_id = prop_data['sq__ft'].idxmax()
            ax.annotate(f"Max {df2.iloc[max_id]['type']}",
                        xy=(df2.iloc[max_id]['group_num'],
                            df2.iloc[max_id]['sq__ft']),
                        xytext=(df2.iloc[max_id]['group_num'],
                                df2.iloc[max_id]['sq__ft']),
                        arrowprops=dict(facecolor='black',
                                        headwidth=4,
                                        width=2,
                                        headlength=4),
                        horizontalalignment='left',
                        verticalalignment='top')
            max_id = prop_data['sq__ft'].idxmin()
            ax.annotate(f"Min {df2.iloc[max_id]['type']}",
                        xy=(df2.iloc[max_id]['group_num'],
                            df2.iloc[max_id]['sq__ft']),
                        xytext=(df2.iloc[max_id]['group_num'],
                                df2.iloc[max_id]['sq__ft']),
                        arrowprops=dict(facecolor='black',
                                        headwidth=4,
                                        width=2,
                                        headlength=4),
                        horizontalalignment='left',
                        verticalalignment='top')

    """
    Question 3:
    Create a grid of bar plots with each one representing a single 
    zipcode and in that zipcode the sq_ft distribution is grouped by the 
    category of condo, residential and multi-family, please also include 
    ticks, labels and legend in your plot
    """
    fig, axes = plt.subplots(math.ceil(num_zips / MAX_FIG_COLUMNS),
                             MAX_FIG_COLUMNS, sharex=True, sharey=True)
    max_sq_ft = df2['sq__ft'].max()
    for ax, data in zip(axes.flatten(), groupby_zip):
        ax.bar('Condo',
               data[1][data[1]['type'] == 'Condo']['sq__ft'].mean())
        ax.bar('Residential',
               data[1][data[1]['type'] == 'Residential']['sq__ft'].mean())
        ax.bar('Multi-Family',
               data[1][data[1]['type'] == 'Multi-Family']['sq__ft'].mean())
        ax.set_yticks(range(0, max_sq_ft, max_sq_ft // 5))
        ax.set_title(data[0])
        ax.legend(['Condo', 'Residential', 'Multi-Family'])
        ax.set_ylabel('Square ft')

    """
    Question 4:
    Create a grid of bar plots with each one representing a single 
    zipcode and in that zipcode the price distribution is grouped by the 
    category of condo, residential and multi-family, please also include 
    ticks, labels and legend in your plot
    """

    fig, axes = plt.subplots(math.ceil(num_zips / MAX_FIG_COLUMNS),
                             MAX_FIG_COLUMNS, sharex=True, sharey=True)
    max_sq_ft = df2['price'].max()
    for ax, data in zip(axes.flatten(), groupby_zip):
        ax.bar('Condo',
               data[1][data[1]['type'] == 'Condo']['price'].mean())
        ax.bar('Residential',
               data[1][data[1]['type'] == 'Residential']['price'].mean())
        ax.bar('Multi-Family',
               data[1][data[1]['type'] == 'Multi-Family']['price'].mean())
        ax.set_yticks(range(0, max_sq_ft, max_sq_ft // 5))
        ax.set_title(data[0])
        ax.legend(['Condo', 'Residential', 'Multi-Family'])
        ax.set_ylabel('Price')
    plt.show()

    """
    Question 5:
    Plot the average price distribution based on zipcode for each 
    category of real estate: condo, residential and multi-family, please 
    also include ticks, labels and legend in your plot
    """
    num_zips = df2['zip'].nunique()
    
    ziptype = df2.groupby(['zip','type'])
    for zi, data in ziptype:
        sns.distplot(data['price']).set_title(zi)
        plt.show()
    """
    Question 6:
    Plot the average price distribution based on city for each category 
    of real estate: condo, residential and multi-family, please also 
    include ticks, labels and legend in your plot
    """
    num_cities = df2['city'].nunique()
    
    citytype = df2.groupby(['city', 'type'])
    for city, data in citytype:
        sns.distplot(data['price']).set_title(city)
        plt.show()
    """
    Part 2:
    SP500.csv
    """

    """
    Question 1:
    Plot daily gain/loss for January of 2018, annotate the highest daily 
    gain and its date, the highest daily loss and its date in January 
    2018
    """
    df = pd.read_csv(input_file1, parse_dates=['Date'])
    df['Price Delta'] = df['Adj Close'] - df['Open']
    jangainloss=df['Price Delta']
    
    start_date = "2018-1-1"
    end_date = "2018-1-31"
    after_start_date = df["Date"] >= start_date
    before_end_date = df["Date"] <= end_date
    between_two_dates = after_start_date & before_end_date

    filtered=jangainloss.loc[between_two_dates]
    filtered.plot()

    """
    Question 2:
    Make pair plot matrix of January 2018 SP500 data on high, low, adj 
    close and volumn
    """
    dftime=df.loc[between_two_dates]
    spdata = dftime[['High', 'Low', 'Adj Close', 'Volume']]
    meta_data = np.log(spdata).diff().dropna()
    sns.pairplot(meta_data, diag_kind='kde', plot_kws={'alpha': 0.2})

if __name__ == '__main__':
    main()
