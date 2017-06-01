import requests
import json
from db import Mongo

class BTCC(object):

    def __init__(self):
        self.name = 'BTCC'
        self.url    = 'https://data.btcchina.com/data/ticker?market=btccny'
        self.db     = Mongo()
    
    def tick(self):
        response = requests.get(self.url)
        price = response.json()
        buy = float(price['ticker']['buy'])
        sell = float(price['ticker']['sell']) 
        mid = (buy + sell)/2.0
        print self.name, mid
        return mid, buy, sell
