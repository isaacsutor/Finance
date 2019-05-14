import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['^GSPC', '^IXIC', '^GDAXI']

ind_data = pd.DataFrame()

for t in tickers:
    ind_data[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

# ind_data.head()
# ind_data.tail()

(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()

annual_ind_returns = ind_data.mean() * 250
print(annual_ind_returns)

tickers = ['PG', '^GSPC', '^DJI']
data_2 = pd.DataFrame()

for t in tickers:
    data_2[t] = wb.DataReader(t, datasource='yahoo', start='2007-1-1')['Adj Close']

print(data_2.tail())

(data_2 / data_2.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()