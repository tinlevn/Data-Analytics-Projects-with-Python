"""
By:
Jeremy Devore
Tin Le
"""

import pandas as pd
from pathlib import Path

input_file1 = Path('SP500.csv')
input_file2 = Path('Sacramentorealestatetransactions.csv')
output_file = Path('SP500_sorted.csv')
LINE_WIDTH = 60

def print_report_data(data):
    avg_data = data.mean()
    print(f"Avg Open Price: ${avg_data['Open']:.2f}\n"
          f"Avg Close Price: ${avg_data['Adj Close']:.2f}\n"
          f"Avg Volume: {int(avg_data['Volume'])}\n"
          f"Avg Price Delta: ${avg_data['Price Delta']:.2f}\n")

def main():
    
# Part 1 Stocks
    print("Part 1:")
    df = pd.read_csv(input_file1, parse_dates=['Date'])
    df['Price Delta'] = df['Adj Close'] - df['Open']

# Question 1: Sort daily gain/loss for December of 2018 and store
# the result back to a .csv file
    print(f"{'='*LINE_WIDTH}\nQuestion 1\n{'='*LINE_WIDTH}")
    output_df = df.sort_values('Price Delta').drop('Price Delta', axis=1)
    output_df.to_csv(output_file)
    print("Sorted table saved")
    
# Question 2: Find all of the daily gains reach 20% and above and
# display them
    print(f"{'='*LINE_WIDTH}\nQuestion 2\n{'='*LINE_WIDTH}")
    percent_increase_filter = df['Price Delta'].div(df['Open']) >= 0.2
    print(f"All daily gains 20% and above: \n"
          f"{df[percent_increase_filter]}")
  
# Question 3: Finding the highest gain date and amount and the
# lowest date and amount.
    print(f"{'='*LINE_WIDTH}\nQuestion 3\n{'='*LINE_WIDTH}")

    max_gain_index = df['Price Delta'].idxmax()
    max_loss_index = df['Price Delta'].idxmin()

    print(f"Highest Gain Date: {df.iloc[max_gain_index]['Date']}\n"
          f"Highest Gain Amount: "
          f"${df.iloc[max_gain_index]['Price Delta']:.2f}\n"
          f"Highest Loss Date: "
          f"{df.iloc[max_loss_index]['Date']}\n"
          f"Highest Loss Amount: "
          f"${df.iloc[max_loss_index]['Price Delta']:.2f}")

 # Question 4: Highest daily transaction volume and its date.
    print(f"{'='*LINE_WIDTH}\nQuestion 4\n{'='*LINE_WIDTH}")

    max_volume_index = df['Volume'].idxmax()

    print(f"Max Transaction Volume Date: "
          f"{df.iloc[max_volume_index]['Date']}\n"
          f"Max Transaction Volume: "
          f"{df.iloc[max_volume_index]['Volume']}")

 # Question 5: print a monthly report for the years 2017-2018 and
 # include the monthly open price, close price, transaction volume,
 # gain/loss, and do a query to find all of the months that have a
 # certain range of open prices.
    print(f"{'='*LINE_WIDTH}\nQuestion 5\n{'='*LINE_WIDTH}")
    df = df.set_index('Date')
    report = df.loc['2017':'2018'].groupby(pd.Grouper(freq='M'))
    for time, data in report:
        print(f"{time.strftime('%B %Y')}")
        print_report_data(data)
    # Make query of a certain range in open price
    min_open_price = 2300
    max_open_price = 2400
    print(f"{'='*LINE_WIDTH}\nMonths with open prices between "
          f"${min_open_price} and ${max_open_price}:")
    for time, data in filter(lambda x: min_open_price
                                       <= x[1].mean()['Open']
                                       <= max_open_price, report):
        print(f"{time.strftime('%B %Y')}")
        print_report_data(data)
    
 # Question 6: a yearly report which has annual average open price,
 # close price, transaction volume and gain/loss from 1950 to 2018,
 # and the most profitable year.
    print(f"{'='*LINE_WIDTH}\nQuestion 6\n{'='*LINE_WIDTH}")

    report = df.groupby(pd.Grouper(freq='Y'))
    for year, data in report:
        print(f"{year.strftime('%Y')}")
        print_report_data(data)

    max_profit = sorted(report,
                        key=lambda x: x[1]['Price Delta'].mean())[-1]
    print(f"Most profitable year: {max_profit[0].strftime('%Y')}")

 # Question 7: a every other five year report which has every five
 # year average open price, close price, transaction volume and
 # gain/loss from 1950 to 2018, and the most profitable five year.
    print(f"{'='*LINE_WIDTH}\nQuestion 7\n{'='*LINE_WIDTH}")
    report = df.groupby(pd.Grouper(freq='5YS'))
    for year, data in report:
        print(f"{year.year} - {(year + pd.Timedelta('5 y')).year}")
        print_report_data(data)

    max_profit = sorted(report,
                        key=lambda x: x[1]['Price Delta'].mean())[-1]
    print(f"Most profitable 5 years: "
          f"{max_profit[0].year} - "
          f"{(max_profit[0] + pd.Timedelta('5 y')).year}")

# Part 2 Housing transactions
 # Question 1: Regroup the data first by city name, then by type
    print("Part 2")
    print(f"{'='*LINE_WIDTH}\nQuestion 1\n{'='*LINE_WIDTH}")
    df1 = pd.read_csv(input_file2)
    group_city = df1.groupby(['city'])
    group_type = df1.groupby(['type'])
    print("Grouped")

 # Question 2: For each city, each type, find the highest, median
 # and lowest transactions
    print(f"{'='*LINE_WIDTH}\nQuestion 2\n{'='*LINE_WIDTH}")
    cmin = group_city['price'].min()
    print("The lowest prices in different cities are: \n{}".format(cmin))
    cmed = group_city['price'].median()
    print("Median of transaction for city: \n{}".format(cmed))
    cmax = group_city['price'].max()
    print("The highest price in different cities are: \n{}".format(cmax))


    tmin = group_type['price'].min()
    print("The lowest price in different types are: \n{}".format(tmin))
    tmed = group_type['price'].median()
    print("Median of transaction for type: \n{}".format(tmed))
    tmax = group_type['price'].max()
    print("The highest prices in different types are: \n{}".format(tmax))

 # Question 3: For each zipcode and each type, find average
 # transactions
    print(f"{'='*LINE_WIDTH}\nQuestion 3\n{'='*LINE_WIDTH}")
    zip_mean = pd.pivot_table(df1, values='price',
                              index=pd.Grouper(key='zip'),
                              columns='state')  # mean of each group
    type_mean = pd.pivot_table(df1, values='price',
                               index=pd.Grouper(key='type'),
                               columns='state')
    print(zip_mean)
    print(type_mean)


if __name__ == '__main__':
    main()
