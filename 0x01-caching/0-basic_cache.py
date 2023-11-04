#!/usr/bin/python3
''' class BasicCache '''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache class inheriting frm  Basecaching class '''


    def put(self, key, item):
        ''' put finction '''
        if key is None or item is None:
            return None
        self.cache_data[key] = item


    def get(self, key):
        ''' get function '''
        if key is None:
            return None
        data_key = self.cache_data.get(key)
        return data_key
