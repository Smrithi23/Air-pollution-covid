import numpy as np
import pandas as pd
from data import *

bangalore_df = pd.DataFrame()
chennai_df = pd.DataFrame()
delhi_df = pd.DataFrame()
kolkata_df = pd.DataFrame()
mumbai_df = pd.DataFrame()
bangalore_flag = 0
chennai_flag = 0
delhi_flag = 0
kolkata_flag = 0 
mumbai_flag = 0

for city in cities:
    for factor in factors:
        src = './raw data/pollution/' + city + '/' + factor + '.xlsx'
        print(city, factor)
        df = pd.DataFrame()
        df = pd.read_excel(src, sheet_name = 'Sheet1')
        df.replace('None', np.NaN, inplace=True)
        df.fillna(df.mean(), inplace=True)
        if city == 'bangalore':
            # if bangalore_flag == 0:
            #     bangalore_df['Date'] = df['Date']
            #     bangalore_flag = 1
            bangalore_df[factor + '_avg'] = df.mean(axis = 1).round(3)
            print(bangalore_df.head())
        elif city == 'chennai':
            # if chennai_flag == 0:
            #     chennai_df['Date'] = df['Date']
            #     chennai_flag = 1
            chennai_df[factor + '_avg'] = df.mean(axis = 1).round(3)
            print(chennai_df.head())
        elif city == 'delhi':
            # if delhi_flag == 0:
            #     delhi_df['Date'] = df['Date']
            #     delhi_flag = 1
            delhi_df[factor + '_avg'] = df.mean(axis = 1).round(3)
            print(delhi_df.head())
        elif city == 'kolkata':
            # if kolkata_flag == 0:
            #     kolkata_df['Date'] = df['Date']
            #     kolkata_flag = 1
            kolkata_df[factor + '_avg'] = df.mean(axis = 1).round(3)
            print(kolkata_df.head())
        elif city == 'mumbai':
            # if mumbai_flag == 0:
            #     mumbai_df['Date'] = df['Date']
            #     mumbai_flag = 1
            mumbai_df[factor + '_avg'] = df.mean(axis = 1).round(3)
            print(mumbai_df.head())

# bangalore_df.to_csv('./test/bangalore_pollution.csv')
# chennai_df.to_csv('./test/chennai_pollution.csv')
# delhi_df.to_csv('./test/delhi_pollution.csv')
# kolkata_df.to_csv('./test/kolkata_pollution.csv')
# mumbai_df.to_csv('./test/mumbai_pollution.csv')

dataframe = pd.read_csv('./raw data/covid/districts.csv')
bangalore_covid_df = pd.DataFrame()
chennai_covid_df = pd.DataFrame()
delhi_covid_df = pd.DataFrame()
kolkata_covid_df = pd.DataFrame()
mumbai_covid_df = pd.DataFrame()

for index, row in dataframe.iterrows():

        if row['District'] == 'Bengaluru Urban':
            bangalore_covid_df = bangalore_covid_df.append(pd.Series(row), ignore_index=True)

        elif row['District'] == 'Chennai':
            chennai_covid_df = chennai_covid_df.append(pd.Series(row), ignore_index=True)

        elif row['District'] == 'Delhi':
            delhi_covid_df = delhi_covid_df.append(pd.Series(row), ignore_index=True)

        elif row['District'] == 'Kolkata':
            kolkata_covid_df = kolkata_covid_df.append(pd.Series(row), ignore_index=True)

        elif row['District'] == 'Mumbai':
            mumbai_covid_df = mumbai_covid_df.append(pd.Series(row), ignore_index=True)

def combine_pollution_covid(city_name, covid_df, pollution_df):
    covid_df = covid_df.iloc[5:432, 0:]
    covid_df = covid_df.reset_index()
    pollution_df = pollution_df.iloc[121:548, 0:]
    pollution_df = pollution_df.reset_index()
    dataframe = pd.concat([pd.DataFrame(covid_df, columns=['Date']), pollution_df, pd.DataFrame(covid_df, columns=['Confirmed', 'Recovered', 'Deceased'])], axis=1)
    dataframe.drop('index', inplace=True, axis=1)
    dataframe.to_csv('./data/' + city_name + '.csv')

# bangalore_covid_df.to_csv('./test/bangalore_covid.csv')
# chennai_covid_df.to_csv('./test/chennai_covid.csv')
# delhi_covid_df.to_csv('./test/delhi_covid.csv')
# kolkata_covid_df.to_csv('./test/kolkata_covid.csv')
# mumbai_covid_df.to_csv('./test/mumbai_covid.csv')

combine_pollution_covid('bangalore', bangalore_covid_df, bangalore_df)
print('>> Finished processing final bengaluru pollution covid data')
combine_pollution_covid('chennai', chennai_covid_df, chennai_df)
print('>> Finished processing final chennai pollution covid data')
combine_pollution_covid('delhi', delhi_covid_df, delhi_df)
print('>> Finished processing final delhi pollution covid data')
combine_pollution_covid('kolkata', kolkata_covid_df, kolkata_df)
print('>> Finished processing final kolkata pollution covid data')
combine_pollution_covid('mumbai', mumbai_covid_df, mumbai_df)
print('>> Finished processing final mumbai pollution covid data')