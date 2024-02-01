#!/usr/bin/env python3
'''
BasicCache module
'''
Basecaching = __import__('base_caching').BaseCaching


class BasicCache (Basecaching):
    '''
    BasicCache class
    '''
    def put(self, key, item):
        '''
        Put method
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        Get method
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
