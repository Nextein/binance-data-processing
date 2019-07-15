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


def clean(candles):
    data = pd.DataFrame(candles, columns=['open time',
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
                                          'ignore'])
    data.pop('close time')
    data.pop('asset volume')
    data.pop('base buy volume')
    data.pop('quote buy volume')
    data.pop('ignore')


    data['open time'] = pd.to_datetime(data['open time'], unit='ms')
    return data


def get_historical_data(symbol, interval, start, end):
    client = new_client('test')
    candles = client.get_historical_klines(symbol=symbol, interval=interval, start_str=start, end_str=end)
    data = pd.DataFrame(candles, columns=['open time',
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
                                          'ignore'])

    data.pop('close time')
    data.pop('asset volume')
    data.pop('base buy volume')
    data.pop('quote buy volume')
    data.pop('ignore')
    data.pop('# trades')
    data.pop('volume')
    data['open time'] = pd.to_datetime(data['open time'], unit='ms')
    print(data['open time'].head(15))
    return data


time_to_secs = {
    '1m': 60,
    '3m': 180,
    '5m': 300,
    '15m': 900,
    '30m': 1800,
    '1h': 3600,
    '2h': 7200,
    '4h': 14400,
    '6h': 21600,
    '8h': 28800,
    '12h': 43200,
    '1d': 86400,
    '3d': 259200,
    '1w': 604800,
    '1M': 2592000
}
