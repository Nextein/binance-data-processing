import configparser
import pandas as pd
parser = configparser.ConfigParser()
parser.read("params.settings")

data = pd.read_csv(parser.get('EMA', 'datapath'))
data.columns = ['open', 'high', 'low', 'close', 'volume', '# trades']
print("data fetched")

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

returns = 0
for i in range(1,len(greater)):
    if greater[i] == 1 and greater[i-1] == 0:
        buy = price[i]
        print("BUY - {}".format(buy))
    elif greater[i] == 0 and greater[i-1] == 1:
        return_ = (price[i]/buy)-1
        print("SELL - {} === {}".format(price[i], return_))
        returns += return_

print(returns)