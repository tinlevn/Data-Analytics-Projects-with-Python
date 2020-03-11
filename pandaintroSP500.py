#Group Members: Jeremy Devore, Tin Le

import numpy as np
import pandas as pd
from pathlib import Path

input_file = Path('SP500.csv')
LINE_WIDTH = 60

#Print fucntion
def print_report_data(data):
    avg_data = data.mean()
    print(f"Avg Open Price: ${avg_data['Open']:.2f}\n"
          f"Avg Close Price: ${avg_data['Adj Close']:.2f}\n"
          f"Avg Volume: {int(avg_data['Volume'])}\n"
          f"Avg Price Delta: ${avg_data['Price Delta']:.2f}\n")

#Main definition
def main():
    df = pd.read_csv(input_file, parse_dates=['Date'])
    df['Price Delta'] = df['Adj Close'] - df['Open']
# Question 1: Finding the highest gain date and amount and the
# lowest date and amount.
    print(f"{'='*LINE_WIDTH}\nQuestion 1\n{'='*LINE_WIDTH}")

    max_gain_index = df['Price Delta'].idxmax()
    max_loss_index = df['Price Delta'].idxmin()

    print(f"Highest Gain Date: {df.iloc[max_gain_index]['Date']}\n"
          f"Highest Gain Amount: "
          f"${df.iloc[max_gain_index]['Price Delta']:.2f}\n"
          f"Highest Loss Date: "
          f"{df.iloc[max_loss_index]['Date']}\n"
          f"Highest Loss Amount: "
          f"${df.iloc[max_loss_index]['Price Delta']:.2f}")

# Question 2: Highest daily transaction volume and its date.
    print(f"{'='*LINE_WIDTH}\nQuestion 2\n{'='*LINE_WIDTH}")

    max_volume_index = df['Volume'].idxmax()

    print(f"Max Transaction Volume Date: "
          f"{df.iloc[max_volume_index]['Date']}\n"
          f"Max Transaction Volume: "
          f"{df.iloc[max_volume_index]['Volume']}")

# Question 3: print a monthly report for the years 2017-2018 and
# include the monthly open price, close price, transaction volume,
# gain/loss, and do a query to find all of the months that have a
# certain range of open prices.
    print(f"{'='*LINE_WIDTH}\nQuestion 3\n{'='*LINE_WIDTH}")
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
    
# Question 4: a yearly report which has annual average open price,
# close price, transaction volume and gain/loss from 1950 to 2018,
# and the most profitable year.
    print(f"{'='*LINE_WIDTH}\nQuestion 4\n{'='*LINE_WIDTH}")

    report = df.groupby(pd.Grouper(freq='Y'))
    for year, data in report:
        print(f"{year.strftime('%Y')}")
        print_report_data(data)

    max_profit = sorted(report,
                        key=lambda x: x[1]['Price Delta'].mean())[-1]
    print(f"Most profitable year: {max_profit[0].strftime('%Y')}")

# Question 5: a every other five year report which has every five
# year average open price, close price, transaction volume and
# gain/loss from 1950 to 2018, and the most profitable five year.
    print(f"{'='*LINE_WIDTH}\nQuestion 5\n{'='*LINE_WIDTH}")
    report = df.groupby(pd.Grouper(freq='5YS'))
    for year, data in report:
        print(f"{year.year} - {(year + pd.Timedelta('5 y')).year}")
        print_report_data(data)

    max_profit = sorted(report,
                        key=lambda x: x[1]['Price Delta'].mean())[-1]
    print(f"Most profitable 5 years: "
          f"{max_profit[0].year} - "
          f"{(max_profit[0] + pd.Timedelta('5 y')).year}")

if __name__ == '__main__':
    main()
