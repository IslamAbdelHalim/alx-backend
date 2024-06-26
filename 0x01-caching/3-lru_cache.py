#!/usr/bin/python3
"""
    LRU Caching
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
        LRU Cashing
    """

    def __init__(self):
        """
            init method
        """
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        """
            put method
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
                theKey = self.cache_data.popitem(last=False)[0]
                print('DISCARD: ' + theKey)

    def get(self, key):
        """
            get method
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
