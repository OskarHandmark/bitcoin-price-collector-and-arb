import requests
import json
from db import Mongo

class Gemini(object):

    def __init__(self):
        self.name = 'Gemini'
        self.url    = 'https://api.gemini.com/v1/pubticker/btcusd'
        self.db     = Mongo() 

    
    def tick(self):
        response = requests.get(self.url)
        book = response.json()
        buy = float(book['bid'])
        sell = float(book['ask'])
        mid = (buy + sell)/2.0
        return mid, buy, sell