import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print(PG['simple_return'])
PG.head()
PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print(PG['log_return'])

PG['log_return'].plot(figsize=(8, 5))
plt.show()

log_return_d = PG['log_return'].mean()
print(log_return_d)
log_return_a = PG['log_return'].mean() * 250
print(log_return_a)
print(str(round(log_return_a, 5) * 100) + ' %')
