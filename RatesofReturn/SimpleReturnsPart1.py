import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print(PG['simple_return'])
PG['simple_return'].plot(figsize=(8, 5))
# plt.show()

# mean return of PG
avg_returns_d = PG['simple_return'].mean()
print(avg_returns_d)

avg_returns_a = PG['simple_return'].mean() * 250
print(avg_returns_a)

print(str(round(avg_returns_a, 5) * 100) + ' %')
