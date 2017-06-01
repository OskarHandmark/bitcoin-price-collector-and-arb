import requests
import json
from db import Mongo

class Bitstamp(object):

    def __init__(self):
        self.name = 'Bitstamp'
        self.url    = 'https://www.bitstamp.net/api/ticker/'
        self.db     = Mongo()
    
    def tick(self):
        response = requests.get(self.url)
        price = response.json()
        buy = float(price['bid'])
        sell = float(price['ask'])
        mid = (buy + sell)/2.0
        return mid, buy, sell
