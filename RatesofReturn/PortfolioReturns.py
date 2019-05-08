import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import pandas as pd

tickers = ['PG', 'MSFT', 'F', 'GE']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

mydata.info()
# mydata.head()
# mydata.tail()

print(mydata.iloc[0])

# Normalized so that each starts at 0 to be able to compare performance
(mydata / mydata.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()

# Not normalized just to see difference
mydata.plot(figsize=(15, 6))
plt.show()

# labels : dates
# mydata.loc('1995-01-03')
# positions
# mydata.iloc[0]

# Calculate the the Portfolio
returns = (mydata / mydata.shift(1)) - 1
# returns.head()
weights = np.array([0.25, 0.25, 0.25, 0.25])
# this uses daily returns not the average annual return
np.dot(returns, weights)

annual_returns = returns.mean() * 250
print(annual_returns)
print(np.dot(annual_returns, weights))
var = np.dot(annual_returns, weights)
pfolio_1 = str(round(var, 5) * 100) + ' %'
print(pfolio_1)

weights_2 = np.array([0.4, 0.4, 0.15, 0.05])
pfolio_2 = str(round(np.dot(annual_returns, weights_2), 5) * 100) + ' %'
print(pfolio_1)
print(pfolio_2)

