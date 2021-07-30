import numpy as np
import pandas as pd
from data import *

class City:
    def __init__(self, city_name):
        self.name           = city_name
        self.df             = pd.DataFrame(columns=['Date', 'Confirmed', 'Recovered', 'Deceased'])
        self.temp_df        = pd.DataFrame(columns=['Date', 'State', 'District', 'Confirmed', 'Recovered', 'Deceased', 'Other', 'Tested'])
        self.flag           = 0
        self.confirmed      = 0
        self.recovered      = 0
        self.deceased       = 0

def clean_pollution_data(city, city_name):
    df = []
    i = 0
    for district in city:
        df.append(pd.read_excel('./pollution files/' + city_name + '/' + district + '.xlsx', sheet_name = 'Sheet1'))
        df[i].replace('None', np.NaN, inplace=True)
        df[i].fillna(df[i].mean(), inplace=True)
        i += 1
    data = pd.concat([df[0]['Date'], pd.concat(df).groupby(level=0).mean().round(2)], axis=1)
    data.to_excel('./pollution data/' + city_name + '.xlsx')
    print('>> Processed ' + city_name +' pollution data')

def clean_covid_data(city, row):
    if city.name == 'Bengaluru':
        if row['District'] == 'Bengaluru Rural':
            city.temp_df = row
        elif row['District'] == 'Bengaluru Urban':
            new_row                     = {}
            new_row['Date']             = row['Date']
            new_row['Recovered']        = row['Recovered'] + city.temp_df['Confirmed']
            new_row['Deceased']         = row['Deceased'] + city.temp_df['Confirmed']
            new_row['Confirmed']        = row['Confirmed'] + city.temp_df['Confirmed']
            city.df                     = city.df.append(pd.Series(new_row), ignore_index=True)
    else:
        new_row                     = {}
        new_row['Date']             = row['Date']
        new_row['Confirmed']        = row['Confirmed']
        new_row['Recovered']        = row['Recovered']
        new_row['Deceased']         = row['Deceased']
        city.df                     = city.df.append(pd.Series(new_row), ignore_index=True)

df = pd.read_csv('./covid data/districts.csv')

bengaluru_covid_data   = City('Bengaluru')
chennai_covid_data     = City('Chennai')
delhi_covid_data       = City('Delhi')
kolkata_covid_data     = City('Kolkata')
mumbai_covid_data      = City('Mumbai')

clean_pollution_data( bengaluru, "bengaluru")
clean_pollution_data( chennai,   "chennai"  )
clean_pollution_data( delhi,     "delhi"    )
clean_pollution_data( kolkata,   "kolkata"  )
clean_pollution_data( mumbai,    "mumbai"   )

print("\n")

for index, row in df.iterrows():

        if row['District'] == 'Bengaluru Rural' or row['District'] == 'Bengaluru Urban':
            clean_covid_data(bengaluru_covid_data, row)

        elif row['District'] == 'Chennai':
            clean_covid_data(chennai_covid_data, row)

        elif row['District'] == 'Delhi':
            clean_covid_data(delhi_covid_data, row)

        elif row['District'] == 'Kolkata':
            clean_covid_data(kolkata_covid_data, row)

        elif row['District'] == 'Mumbai':
            clean_covid_data(mumbai_covid_data, row)

bengaluru_covid_data.df.to_excel("./covid data/bengaluru.xlsx")
print('>> Processed bengaluru covid data')
chennai_covid_data.df.to_excel("./covid data/chennai.xlsx")
print('>> Processed chennai covid data')
delhi_covid_data.df.to_excel("./covid data/delhi.xlsx")
print('>> Processed delhi covid data')
kolkata_covid_data.df.to_excel("./covid data/kolkata.xlsx")
print('>> Processed kolkata covid data')
mumbai_covid_data.df.to_excel("./covid data/mumbai.xlsx")
print('>> Processed mumbai covid data')

print("\n")
print(">> Processing final files for the deep learning model")
print("\n")

def combine_pollution_covid(city_name):
    covid_df = pd.read_excel("./covid data/" + city_name + ".xlsx")
    pollution_df = pd.read_excel('./pollution data/' + city_name + ".xlsx")
    covid_df = covid_df.iloc[4:370, 1:]
    covid_df = covid_df.reset_index()
    pollution_df = pollution_df.iloc[121:487, 2:]
    pollution_df = pollution_df.reset_index()
    dataframe = pd.concat([covid_df, pollution_df], axis=1)
    dataframe.drop('index', inplace=True, axis=1)
    dataframe.to_csv('./data/' + city_name + '.csv')

combine_pollution_covid('bengaluru')
print('>> Finished processing final bengaluru pollution covid data')
combine_pollution_covid('chennai')
print('>> Finished processing final chennai pollution covid data')
combine_pollution_covid('delhi')
print('>> Finished processing final delhi pollution covid data')
combine_pollution_covid('kolkata')
print('>> Finished processing final kolkata pollution covid data')
combine_pollution_covid('mumbai')
print('>> Finished processing final mumbai pollution covid data')