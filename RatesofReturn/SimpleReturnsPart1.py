import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print(PG['simple_return'])
