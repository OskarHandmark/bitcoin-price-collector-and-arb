import time
import sys
import json
from db import Mongo
import matplotlib.pyplot as plt
import numpy

class Runner(object):

    def __init__(self):
        self.db = Mongo()
        self.short = 'Okcoincny'
        self.long = 'BTCC'
        
    def plot(self):
        DIFFS, LONG_PRICES, SHORT_PRICES = self.db.get_diffs_and_prices(self.short, self.long)
        plt.plot(DIFFS)
        plt.show()
    
    def plot_prices(self):
        DIFFS, LONG_PRICES, SHORT_PRICES = self.db.get_diffs_and_prices(self.short, self.long)
        plt.plot(LONG_PRICES, 'g')
        plt.plot(SHORT_PRICES, 'r')
        plt.show()

if __name__ == "__main__":
    # Runner().plot()
    Runner().plot_prices()
