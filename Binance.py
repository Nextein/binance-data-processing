from binance.client import Client
import configparser
import pandas as pd

transaction_commission = 0.00075
total_commission = 0.0015

def new_client(name):
    parser = configparser.ConfigParser()
    parser.read("clients.private")
    client = Client(api_key=parser.get(name, 'API_key'), api_secret=parser.get(name, 'secret_key'))
    return client


def get_historical_data(symbol, interval, start, end):
    client = new_client('test')
    candles = client.get_historical_klines(symbol=symbol, interval=interval, start_str=start, end_str=end )
    data = pd.DataFrame(candles, columns= ['open time', 'open', 'high', 'low', 'close', 'volume', 'close time', 'asset volume', '# trades', 'base buy volume', 'quote buy volume', 'ignore'])

    data.pop('close time')
    data.pop('asset volume')
    data.pop('base buy volume')
    data.pop('quote buy volume')
    data.pop('ignore')

    data['open time'] = pd.to_datetime(data['open time'], unit='ms')
    data.set_index('open time', inplace=True)

    return data
