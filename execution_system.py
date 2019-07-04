"""
Live system that runs the entire system on every candle.
"""

import configparser
import time
import Binance

# Params:
parser = configparser.ConfigParser()
parser.read("params.settings")
interval = parser.get('live_system', 'timeframe')

while True:
    # TODO - make the loop start at end of candle so the sleeping makes it trigger on end of each candle
    # Run system
    time.sleep(Binance.time_to_secs(interval))
