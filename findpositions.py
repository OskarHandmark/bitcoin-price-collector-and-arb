import time
import sys
import json
from db import Mongo
import matplotlib.pyplot as plt
import numpy

class Runner(object):
    def __init__(self):
        self.db = Mongo()
        
    def run(self):
        DIFFS, LONG_PRICES, SHORT_PRICES = self.db.get_diffs_and_prices('Okcoincny', 'BTCC')
        
        funds = 500
        BTC = 500
        profit = 0
        short_order = 0
        long_order = 0
        position = False
        for i, diff in enumerate(DIFFS):
            if not position:
                if diff < -0.28:
                    long_order = LONG_PRICES[i]
                    short_order = SHORT_PRICES[i]
                    position = True
                    print 'Entering position. LONG: ', long_order, 'SHORT', short_order
            else:
                if diff > -0.24:
                    long_profit = LONG_PRICES[i] - long_order
                    short_profit = short_order - SHORT_PRICES[i]
                    profit += long_profit + short_profit
                    position = False
                    print 'Exiting position. LONG: ', LONG_PRICES[i], 'SHORT', SHORT_PRICES[i], 'profit: ', long_profit, short_profit, ' => TOTAL: ', long_profit + short_profit
                    print
        print 'profit: ', profit

if __name__ == "__main__":
    # Runner().plot()
    Runner().run()