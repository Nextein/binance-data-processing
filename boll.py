import pandas as pd
import sys
import numpy as np
def bollinger_bands(close, window_size, num_of_std):

    print(close.shape)
    

    close['30 Day MA'] = close['close'].rolling(window=20).mean()
    close['30 Day STD'] = close['close'].rolling(window=20).std()
    close['Upper Band'] = close['30 Day MA'] + (close['30 Day STD'] * 2)
    close['Lower Band'] = close['30 Day MA'] - (close['30 Day STD'] * 2)

    rolling_mean = close.astype(float).rolling(window=window_size).mean()
    rolling_std = close.astype(float).rolling(window=window_size).std()

    print(rolling_mean.shape)
    print(rolling_std.shape)

    upper_band = rolling_mean + (rolling_std * num_of_std)
    lower_band = rolling_mean - (rolling_std * num_of_std)

    return rolling_mean, upper_band, lower_band


start = "1 Jan 2018"
end = "31 Jan 2018"
interval = '1m'
data = pd.read_csv("data/01-2018/BTCUSDT_1-2018.csv", names=['Open_time','Open','High','Low','Close','Volume','Close_time','Quote_asset_volume','Number_of_trades','Taker_buy_base_asset_volume','Taker_buy_quote_asset_volume'])
data.pop("Open_time")
data.pop('Close_time')
data.pop("Quote_asset_volume")
data.pop("Taker_buy_base_asset_volume")
data.pop("Taker_buy_quote_asset_volume")
print("data fetched.")


close1 = float(data['Close'][2])
close = data['Close'].values
# close = np.array(data['Close'].values)
print(close)
close = close[1:]
print(close)
close = np.vectorize(float, close)
close = pd.DataFrame(close)['close']
print(close1)
print('8'*40)
middle, upper, lower = bollinger_bands(close, 20, 2)
below = close < lower.values
buySet = []
sellSet = []
for i in range(len(below)-1):
    if below[i]:
        buySet.append(float(close[i]))
        sellSet.append(float(close[i+1]))

gains = 1
max_gains = 0
for i in range(len(buySet)):
    gains *= sellSet[i]/buySet[i]
    if gains > max_gains:
        max_gains = gains
f = open("boll.log", 'a')
sys.stdout = f

print("=-"*40)
print("Date:\t{}\t{}\ninterval - {}".format(start,end,interval))
print("max_gains:\t{}".format(max_gains))
print("gains:\t{}".format(gains))

bench = float(close[-1])/float(close[0])
print("Benchmark:\t{}".format(bench))
f.close()




