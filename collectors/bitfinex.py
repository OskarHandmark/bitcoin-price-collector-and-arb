import requests
import json
from db import Mongo

class Bitfinex(object):

    def __init__(self):
        self.name = 'Bitfinex'
        self.url    = 'https://api.bitfinex.com/v1/pubticker/btcusd'
        self.db     = Mongo()
        
    
    def tick(self):
        response = requests.get(self.url)
        price = response.json()
        buy = float(price['bid'])
        sell = float(price['ask'])
        mid = float(price['mid'])
        return mid, buy, sell