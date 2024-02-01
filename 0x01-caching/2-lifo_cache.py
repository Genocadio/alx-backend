#!/usr/bin/env python3
'''
LIFO caching
'''
Basecaching = __import__('base_caching').BaseCaching


class LIFOCache(Basecaching):
    """ LIFOCache class """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.last = []

    def put(self, key, item):
        """ Assign to the dictionary """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.last.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.last[-1]]
                    print("DISCARD: {}".format(self.last[-1]))
                    self.last.remove(self.last[-1])
                self.cache_data[key] = item
            self.last.append(key)

    def get(self, key):
        """ Return the value linked """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
