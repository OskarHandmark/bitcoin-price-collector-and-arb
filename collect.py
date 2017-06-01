import time
import sys
import json
from db import Mongo

class Collector(object):

    def __init__(self):
        self.exchanges  = []
        self.db         = Mongo()
        self.shortable  = {}
        
    def start(self):
        collectors_module = __import__('collectors')
        with open('exchanges.json', 'r') as f:
            exchanges = json.loads(f.read())
            for active in exchanges['active']:
                name = active['name']
                exchange = getattr(collectors_module, name)
                self.shortable[name] = active['shortable']
                self.exchanges.append(exchange())
        self.run()

    def calcdiffs(self, data):
        diffs = []
        
        for tick in data['ticks']:
            short_name = tick['name']
            if self.shortable[short_name]:
                price = tick['mid']
                diff_list = []
                for tick in data['ticks']:
                    name = tick['name']
                    if name is not short_name:
                        mid = tick['mid']
                        diff_list.append({
                            "name": name,
                            "price": mid,
                            "diff": 100 * ((float(mid) / float(price)) - 1),
                            "averages": []
                        })
                diffs.append({
                    "short_name": short_name,
                    "price": price,
                    "diffs": diff_list
                })
        data['diffs'] = diffs

    def run(self):
        while True:
            start = time.time()
            data = {
                'ticks': []
            }
            for exchange in self.exchanges:
                mid, buy, sell = exchange.tick()
                data['ticks'].append({
                    "name": exchange.name,
                    "mid": mid,
                    "buy": buy,
                    "sell": sell
                })
            self.calcdiffs(data)
            self.db.save_tick(data)
            delta = time.time()-start
            if delta < 5.0:
                time.sleep(5.0 - delta)

if __name__ == "__main__":
    Collector().start()