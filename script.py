import numpy as np
import pandas as pd
from pandas import read_excel
from data import *

dataframe = pd.DataFrame(columns=['PM2.5', 'NO', 'NO2', 'NOx', 'SO2'])

df = read_excel('./pollution-data/bengaluru/Bapuji Nagar, Bengaluru - KSPCB.xlsx', sheet_name = 'Sheet1')
df.replace('None', np.NaN, inplace=True)
df.fillna(df.mean(), inplace=True)
df.to_excel("new.xlsx")