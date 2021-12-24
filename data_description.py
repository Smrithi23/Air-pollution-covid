import numpy as np
import pandas as pd
from data import *

bangalore_df = pd.DataFrame()
chennai_df = pd.DataFrame()
delhi_df = pd.DataFrame()
kolkata_df = pd.DataFrame()
mumbai_df = pd.DataFrame()

bangalore_df = pd.read_csv('./data/bangalore.csv', header=0, index_col=0)
chennai_df = pd.read_csv('./data/chennai.csv', header=0, index_col=0)
delhi_df = pd.read_csv('./data/delhi.csv', header=0, index_col=0)
kolkata_df = pd.read_csv('./data/kolkata.csv', header=0, index_col=0)
mumbai_df = pd.read_csv('./data/mumbai.csv', header=0, index_col=0)
print("BANGALORE")
print(bangalore_df.describe().transpose())
print("CHENNAI")
print(chennai_df.describe().transpose())
print("DELHI")
print(delhi_df.describe().transpose())
print("KOLKATA")
print(kolkata_df.describe().transpose())
print("MUMBAI")
print(mumbai_df.describe().transpose())