#!/user/bin/env python3
'''
FIFO caching
'''
Basecaching = __import__('base_caching').BaseCaching


class FIFOCache(Basecaching):
    """ FIFO cache system """

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Assign values to a dictionary """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= Basecaching.MAX_ITEMS:
                    discard = self.queue.pop(0)
                    del self.cache_data[discard]
                    print("DISCARD:", discard)
                self.queue.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """ Return values from a dictionary """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
