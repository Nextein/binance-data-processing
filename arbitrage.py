import Binance

def check_arbitrage4(vc, vb, wc, wb, symb):
    buy = vc/vb
    sell = wc/wb
    if sell > buy:
        print('*'*40)
        print("symbol:\t{}\n\tBuy = {}\nSell = {}".format(symb, buy, sell))



def check_arbitrage3(verbose, ac, ab, bc):

    # Arbitrage in direction 1:
    buy = float(ac['askPrice'])
    sell = float(ab['bidPrice']) * float(bc['bidPrice'])
    if (sell/buy) > 1:
        print('*'*40)
        print("arbitrage3 opportunity: buy {}".format(ac['symbol']))
        if verbose:
            print("\tBuy = {}\nSell = {}".format(buy, sell))
    else:

        if verbose:
            print("no:")
            print("\tBuy = {}\nSell = {}".format(buy, sell))

    # Arbitrage in direction 2:
    sell = float(ac['bidPrice'])
    buy = float(ab['askPrice']) * float(bc['askPrice'])
    if (sell/buy) > 1:
        print('*'*40)
        print("arbitrage3 opportunity: buy {}".format(ac['symbol']))
        if verbose:
            print("\tBuy = {}\nSell = {}".format(buy,sell))
    else:

        if verbose:
            print("no:")
            print("\tBuy = {}\nSell = {}".format(buy,sell))


def arbitrage(WB, WS, BS, verbose=False):  # Different attempt (not sure previous one works)
    """
    Formula:
    (ws - 0.075/100) * (1/wb - 0.075/100) * (1/bs - 0.075/100) > 1
    :param WB: Alt/BTC
    :param WS: Alt/USDT
    :param BS: BTC/USDT
    :param verbose: Determines how much text output you want: a lot or a little
    """
    ws = float(client.get_orderbook_ticker(symbol=WS)['bidPrice'])
    wb = float(client.get_orderbook_ticker(symbol=WB)['askPrice'])
    bs = float(client.get_orderbook_ticker(symbol=BS)['askPrice'])

    sell = ws-0.075/100
    buy = 1 / ( ((1/wb) - 0.075/100) * ((1/bs) - 0.075/100) )

    if sell > buy:
        print("BUY")
        print("{} > {}".format(sell, buy))


client = Binance.new_client("test")
count = 0
while(True):
    arbitrage('WINBTC', 'WINUSDT', 'BTCUSDT', verbose=True)
    if count % 1000000 == 0:
        print(count)
    count += 1




# TODO - ERROR: Only grabs price values once, not for each loop iteration
# a1c = client.get_orderbook_ticker(symbol='WINUSDT')
# a1b = client.get_orderbook_ticker(symbol='WINBTC')
# bc = client.get_orderbook_ticker(symbol='BTCUSDT')
# a2c = client.get_orderbook_ticker(symbol='ADAUSDT')
# a2b = client.get_orderbook_ticker(symbol='ADABTC')
#
# i=0
# while True:
#     check_arbitrage3(False, a1c, a1b, bc)
#     # check_arbitrage3(False, a2c, a2b, bc)
#     # check_arbitrage4(float(a1c['askPrice']), float(a1b['bidPrice']), float(a2c['bidPrice']), float(a2b['askPrice']), a1c['symbol'])
#     # check_arbitrage4(float(a2c['askPrice']), float(a2b['bidPrice']), float(a1c['bidPrice']), float(a1b['askPrice']), a2c['symbol'])
#     if i % 1000000 == 0:
#         print(i)
#     i += 1
# check_arbitrage(False,ac,ab,bc)












