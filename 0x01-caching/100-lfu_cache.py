#!/usr/bin/env python3
'''
LFU caching
'''
Basecaching = __import__('base_caching').BaseCaching


class LFUCache(Basecaching):
    """ LFU cache """

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.lfu = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.lfu.remove(key)
        elif len(self.cache_data) >= Basecaching.MAX_ITEMS:
            discard = self.lfu.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        self.cache_data[key] = item
        self.lfu.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.lfu.remove(key)
        self.lfu.append(key)
        return self.cache_data.get(key)
