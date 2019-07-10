"""
Candle colour sequences probability distribution
"""
import numpy as np
import configparser
import pandas as pd
parser = configparser.ConfigParser()
parser.read("params.settings")

"""
STEPS:
1) generate list of x values (where x is length of that colour sequence
2) generate distribution from this
3) plot to see if info is relevant in any way
4) possibly run this for several datasets to see similarities / compare
"""

# Data from EMA backtesting settings (for example)
data = pd.read_csv(parser.get('EMA', 'datapath'))
data.columns = ['open', 'high', 'low', 'close', 'volume', '# trades']
print("data fetched")

colours = []
for candle in range(1, data.shape[0]):  # TODO - Use numpy arrays to do this in parallel
    if (float(data['open'][candle]) - float(data['close'][candle])) > 0:
        colours.append(1)
    else:
        colours.append(0)

X = []
x = 0
for i in range(1, len(colours)):
    if colours[i] == colours(i-1):
        x += 1
    else:
        X.append(x)
X = np.array(X)

print(np.bincount(X))
print('*'*50)
print(X.mean())
print(X.var())

# TODO - Plot distribution of x using matplotlib (check SPS code for this)
# TODO - RUN SCRIPT TO SEE IF IT WORKS
