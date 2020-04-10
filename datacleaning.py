"""
Tin Le
"""

import pandas as pd
import numpy as np
from pathlib import Path
import re

#Please specify file path to your computer

pd.set_option('display.max_rows', None)
input_file1 = Path('D:\BL-Flickr-Images-Book.csv')
input_file2 = Path('D:\olympics.csv')

def main():
    """
    For the Title column, only keep the title part, remove all of the other parts. 
    If the title is inside a bracket, remove the bracket which encloses the title. 
    If there are multiple …, only keep the words before the first one. 
    If there are multiple periods (.), only keep words before the first one.
    """
    df = pd.read_csv(input_file1)
    #Cleaning Title column
    title_extr = df['Title'].str.extract(r'([^.]*).*', expand=True)
    
    #Selecting non-essential columns to drop
    to_drop = ['Identifier','Edition Statement',
            'Place of Publication',
            'Date of Publication',
           'Publisher','Flickr URL',
           'Issuance type','Corporate Contributors',
           'Shelfmarks','Corporate Author','Former owner','Engraver']
    df.drop(to_drop, inplace=True, axis=1)
    
    """
    For the Author and Contributors columns, only keep the first author, remove all of the other parts. 
    If the author or the contributor has other auxiliary information, remove them. title is inside a bracket,
    remove the bracket which encloses the title. 
    If there are multiple …, only keep the words before the first one. 
    If there are multiple periods (.), only keep words before the first one. 
    For all of the names, they should only have the first letter of the first, middle and last names be capital letter,
    all of the remaining letters should be small case.
    
    """
    #Cleaning Author column using Regular Expression
    aut_extr = df['Author'].str.extract(r'([^.\-]*).*', expand=True)
    #Cleaning contributors' names
    contrib_extr = df['Contributors'].str.extract(r'([^.\-\|]*).*', expand=True)
    df=df.assign(Title=title_extr)
    df=df.assign(Author=aut_extr)
    df=df.assign(Contributors=contrib_extr)
    df['Author']=df['Author'].str.lower()
    df['Author']=df['Author'].str.capitalize()
    df['Contributors']=df['Contributors'].str.lower()
    df['Contributors']=df['Contributors'].str.capitalize()
    #Write to CSV with cleaned data
    df.to_csv('cleanfile.csv', encoding='utf-8')
    
    """
    Part 2
    Drop all of the countries which don’t have gold medals, and save the cleaned one back into a new .csv file.
    Output the top five gold medal countries.
    Output the countries that have all three kinds of medals for both summer and winter games.
    """
    
    df2 = pd.read_csv(input_file2)
    #Countries without gold medal specification
    losers = df2[(df2['2'] == '0') & (df2['7'] == '0')].index
    #Countries with medals for all three categories
    various = df2[(df2['2'] != '0') & (df2['3'] != '0')
                 & (df2['4'] != '0') & (df2['7'] != '0')
                 & (df2['8'] != '0') & (df2['9'] != '0')]
    
    # Delete these row indexes from dataFrame
    new_list=df2.drop(losers , inplace=False)
    df2.drop(df2.index[2],inplace=True)
    df2.drop(df2.index[146],inplace=True)
    
    #Write to CSV file
    new_list.to_csv('country_with_gold.csv', encoding='utf-8')
    
    #Finding total number of gold medals for all countries
    df2['Total Gold'] = df2['2'] + df2['7']
    
    #Group top gold medal countries
    topfive=df2.sort_values(['Total Gold','0'], ascending=False).groupby('0').head()
    
    #Print top five gold medal countries
    print(topfive.head(5))
    
    #Print countries with medals for all categories of summer and winter
    print(various)
    
if __name__ == '__main__':
    main()
