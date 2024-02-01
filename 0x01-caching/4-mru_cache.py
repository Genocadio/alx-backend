#!/usr/bin/env python3
'''
MRU caching
'''
Basecaching = __import__('base_caching').BaseCaching


class MRUCache(Basecaching):
    """ MRU caching system """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.list_name = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.list_name.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                print('DISCARD: {}'.format(self.list_name[-1]))
                del self.cache_data[self.list_name[-1]]
                self.list_name.pop()
            self.list_name.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            self.list_name.remove(key)
            self.list_name.append(key)
            return self.cache_data[key]
        return None
