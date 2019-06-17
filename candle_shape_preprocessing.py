from Binance import *
from sklearn import preprocessing
import numpy as np

"""
f1 = Lower wick of candle %
f2 = Higher wick of candle %
f3 = candle size (high-low)
"""


def create_dataset(interval,symbol):


    data = get_historical_data(symbol=symbol, interval=interval,start="3 year ago", end="now")

    open = data['open'].astype(float).values
    high = data['high'].astype(float).values
    low = data['low'].astype(float).values
    close = data['close'].astype(float).values
    volume = data['volume'].astype(float).values
    oh = np.column_stack((open, high))
    lc = np.column_stack((low, close))
    ohlc = np.column_stack((oh, lc))


    # Feature creation:
    feature_name = "{}_{}_candle_shape.csv".format(interval, symbol)
    f1 = high-low
    ohlc_scaled = preprocessing.MinMaxScaler().fit_transform(ohlc.T)
    ohlc_scaled = ohlc_scaled.T

    X = np.column_stack((ohlc_scaled,f1))

    X = np.delete(X, 1, 1) # Delete columns that are all 1s
    X = np.delete(X, 1, 1) # Delete columns that are all 0s
    X = np.column_stack((X,volume))

    print(X.shape)

    ohlcv = np.column_stack((ohlc,volume))
    np.savetxt("{}_ohlcv_{}.csv".format(interval, symbol), ohlcv, delimiter=',')
    print("OHLCV saved to ohlcv_{}.csv".format(symbol))
    np.savetxt(feature_name, X, delimiter=',')
    print("feature saved to \"{}\"".format(feature_name))
    print("Columns: %open -=- %close -=- candle size -=- volume")

    return X


create_dataset('2h', 'BTCUSDT')




