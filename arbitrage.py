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


client = Binance.new_client("test")

a1c = client.get_orderbook_ticker(symbol='EOSUSDT')
a1b = client.get_orderbook_ticker(symbol='EOSBTC')
bc = client.get_orderbook_ticker(symbol='BTCTUSD')
a2c = client.get_orderbook_ticker(symbol='ADAUSDT')
a2b = client.get_orderbook_ticker(symbol='ADABTC')

i=0
while True:
    # check_arbitrage3(False, a1c, a1b, bc)
    # check_arbitrage3(False, a2c, a2b, bc)
    check_arbitrage4(float(a1c['askPrice']), float(a1b['bidPrice']), float(a2c['bidPrice']), float(a2b['askPrice']), a1c['symbol'])
    check_arbitrage4(float(a2c['askPrice']), float(a2b['bidPrice']), float(a1c['bidPrice']), float(a1b['askPrice']), a2c['symbol'])
    if i % 1000000 == 0:
        print(i)
    i += 1
# check_arbitrage(False,ac,ab,bc)












