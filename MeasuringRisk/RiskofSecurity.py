import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['PG', 'BEI.DE']
sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']

# sec_data.tail()
sec_returns = np.log(sec_data / sec_data.shift(1))

print(sec_returns)

# PG
sec_returns['PG'].mean()
sec_returns['PG'].mean() * 250
sec_returns['PG'].std()
sec_returns['PG'].std() * 250 ** 0.5

# Beierdorf
sec_returns['BEI.DE'].mean()
sec_returns['BEI.DE'].mean() * 250
sec_returns['BEI.DE'].std()
sec_returns['BEI.DE'].std() * 250 ** 0.5

# Covariance and Correlation
PG_var = sec_returns['PG'].var()
print(PG_var)

BEI_var = sec_returns['BEI.DE'].var()
print(BEI_var)

PG_var_a = sec_returns['PG'].var * 250

BEI_var_a = sec_returns['BEI.DE'].var() * 250


# Cov
cov_matrix = sec_returns.cov()
print(cov_matrix)

cov_matrix_a = sec_returns.cov() * 250
print(cov_matrix_a)


# correlation
corr_matrix = sec_returns.corr()
print(corr_matrix)


# Calculating Portfolio Risk
weights = np.array([0.5, 0.5])

pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))
print(pfolio_var)

pfolio_vol = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))) ** 0.5
print(str(round(pfolio_vol, 5) * 100) + ' %')



