from pymongo import MongoClient
import json

class Mongo(object):
    """MongoDB database wrapper"""

    def __init__(self, host = "localhost", port = 27017):
        self.client     = MongoClient(host, port)
        self.db         = self.client.penguin
        
    def save_tick(self, book):
        self.db.ticks.insert_one(book)
    
    def get_ticks(self, limit=0):
        return self.db.ticks.find().sort("_id", 1).limit(limit)
    
    def export(self, name, data):
        self.db[name].insert({'data': data})
    
    def get_diffs_and_prices(self, short, longd):
        DIFFS = []
        LONG_PRICES = []
        SHORT_PRICES = []
        
        for tick in self.get_ticks():
            diffs = [diff for diff in tick['diffs'] if diff['short_name'] == short][0]
            SHORT_PRICES.append(diffs['price'])

            for d in diffs['diffs']:
                if d['name'] == longd:
                    DIFFS.append(d['diff'])
                    LONG_PRICES.append(d['price'])
        return DIFFS, LONG_PRICES, SHORT_PRICES