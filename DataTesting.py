import numpy as np
import pandas as pd
from pandas_datareader import data as wb
# this is like a dictionary
ser = pd.Series(np.random.random(5), name = "Column 01")
print(ser)
print(ser[2])
# get data on Proctor and Gamble from Yahoo Starting at the date 1/1/1995
PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
print(PG)
