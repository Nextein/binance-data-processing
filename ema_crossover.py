import configparser
import pandas as pd
import Binance
parser = configparser.ConfigParser()
parser.read("params.settings")

data = pd.read_csv(parser.get('EMA', 'datapath'))
data.columns = ['open time',
                'open',
                'high',
                'low',
                'close',
                'volume',
                'close time',
                'asset volume',
                '# trades',
                'base buy volume',
                'quote buy volume',
                'ignore']
data.pop('close time')
data.pop('asset volume')
data.pop('base buy volume')
data.pop('quote buy volume')
data.pop('ignore')
# data columns: open, high, low, close, volume, # trades
print("data fetched and cleaned")

print(data[:100])
price = data['close'].values
length_ema1 = int(parser.get('EMA', 'ema1'))
length_ema2 = int(parser.get('EMA', 'ema2'))

emaA = data['close'].ewm(span=length_ema1, adjust=False).mean()
emaB = data['close'].ewm(span=length_ema2, adjust=False).mean()

greater = []
for candle in range(len(price)):
    if emaA[candle] > emaB[candle]:
        greater.append(1)
    else:
        greater.append(0)
# print(greater[:100])
print(emaA[:100])
print(emaB[:100])
