from pyalgotrade import strategy
from pyalgotrade.barfeed import quandlfeed

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        super(strategy, self).__init__(feed)
        self.instrument = instrument

    def onBars(self, bars):  # Called for every bar on the feed
        bar = bars[self.instrument]
        self.info(bar.getClose())


# Load the bar feed from CSV file
feed = quandlfeed.Feed()
feed.addBarsFromCSV("CDTBTC", "data/CDTBTC_1d.csv")

# Evaluate the strategy with the feed's bars:
myStrategy = MyStrategy(feed, "CDTBTC")
myStrategy.run()
