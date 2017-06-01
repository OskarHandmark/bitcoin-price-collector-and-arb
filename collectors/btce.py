import requests
import json
from db import Mongo

class Btce(object):

    def __init__(self):
        self.name = 'Btce'
        self.url    = 'https://btc-e.com/api/3/ticker/btc_usd'
        self.db     = Mongo() 

    
    def tick(self):
        response = requests.get(self.url)
        price = response.json()
        buy = float(price['btc_usd']['buy'])
        sell = float(price['btc_usd']['sell'])
        mid = (buy + sell)/2.0
        return mid, buy, sell