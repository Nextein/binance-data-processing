import Binance
import sys
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import numpy as np
import pandas as pd
from sklearn import *


register_matplotlib_converters()
# ========================
# Backtesting
# ========================
start = "29 Apr 2019"
end = "13 May 2019"
verbose = False
interval = '1m'
data = Binance.get_historical_data('BTCUSDT', interval, start, end)
np.savetxt("1m_may_2019.csv", data.astype(float).values, delimiter=',')
# names = ['open', 'high', 'low', 'close', 'volume', '# trades']
# data = pd.read_csv("1m_may_2018.csv", names=names)

print("data fetched.")
price = data['close'].values
best_gains_ema = (0,0)
best_max_gains_ema = (0,0)
best_gains = 0
best_max_gains = 0
for ema1 in range(1,15):
    for ema2 in range(15, 40):
        emaA = data.ewm(span=ema1, adjust=False).mean()
        emaB = data.ewm(span=ema2, adjust=False).mean()
        emaA = emaA['close'].values
        emaB = emaB['close'].values

        greater = emaA > emaB

        buySet = []
        sellSet = []
        for i in range(len(greater)):
            if greater[i]:
                buySet.append(float(price[i]))
                sellSet.append(0)
            else:
                sellSet.append(float(price[i]))
                buySet.append(0)

        gains = 1
        BUY = []
        max_gains = 0
        assert(len(buySet) == len(sellSet))
        for i in range(28, len(buySet)):
            if buySet[i]>0 and buySet[i-1]==0:
                BUY.append(buySet[i])
            elif sellSet[i]>0 and sellSet[i-1]==0 and len(BUY)>0:
                # Execute sell order -> new_capital
                gains = (sellSet[i] / BUY[-1]) * gains
                if gains>max_gains:
                    max_gains = gains
        if verbose:
            print('*'*30)
            print("ema{} + ema{}".format(ema1, ema2))
            print("result - {}".format(gains))
            print("max - {}".format(max_gains))

        if gains > best_gains:
            best_gains = gains
            best_gains_ema = (ema1, ema2)
        if max_gains > best_max_gains:
            best_max_gains = max_gains
            best_max_gains_ema = (ema1, ema2)
f = open("ema.log", 'a')
sys.stdout = f

print("=-"*40)
print("Date:\t{}\t{}\ninterval - {}".format(start,end,interval))
print("\t\t  Features")
print("best max:\t{}+{} - {}".format(best_max_gains_ema[0], best_max_gains_ema[1], best_max_gains))
print("best gains:\t{}+{} - {}".format(best_gains_ema[0], best_gains_ema[1], best_gains))

bench = float(price[-1])/float(price[0])
print("Benchmark:\t{}".format(bench))
f.close()




