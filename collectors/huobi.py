import requests
import json
from db import Mongo

class Huobi(object):

    def __init__(self):
        self.name = 'Huobi'
        self.url    = 'https://api.huobi.com/staticmarket/ticker_btc_json.js'
        self.db     = Mongo()
    
    def tick(self):
        response = requests.get(self.url)
        price = response.json()
        buy = float(price['ticker']['buy'])
        sell = float(price['ticker']['sell']) 
        mid = (buy + sell)/2.0
        print self.name, mid
        return mid, buy, sell
            