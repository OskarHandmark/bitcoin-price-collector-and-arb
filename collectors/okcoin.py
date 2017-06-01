import requests
import json
from db import Mongo

class Okcoin(object):

    def __init__(self):
        self.name = 'Okcoin'
        self.url    = 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd'
        self.db     = Mongo() 

    
    def tick(self):
        response = requests.get(self.url)
        price = response.json()
        buy = float(price['ticker']['buy'])
        sell = float(price['ticker']['sell']) 
        mid = (buy + sell)/2.0
        print self.name, mid
        return mid, buy, sell