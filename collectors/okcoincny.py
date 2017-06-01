import requests
import json
from db import Mongo

class Okcoincny(object):

    def __init__(self):
        self.name = 'Okcoincny'
        self.url    = 'https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny'
        self.db     = Mongo() 

    def tick(self):
        response = requests.get(self.url)
        book = response.json()
        buy = float(book['ticker']['buy'])
        sell = float(book['ticker']['sell']) 
        mid = (buy + sell)/2.0
        print self.name, mid
        return mid, buy, sell