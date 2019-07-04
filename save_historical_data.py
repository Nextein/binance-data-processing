import Binance
import numpy as np


start = "13 Nov 2017"
end = "Now"
interval = '15m'
ticker = 'CDTBTC'

data = Binance.get_historical_data(ticker, interval, start, end)

np.savetxt("data/{}_{}.csv".format(ticker, interval), data.astype(float).values, delimiter=',')

print("\ndata stored.")
