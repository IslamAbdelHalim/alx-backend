#!/usr/bin/python3
"""
    LRU Caching
"""


from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
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
        if not (key and item):
            return None
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f'DISCARD: {list(self.cache_data.keys())[-2]}')
            del self.cache_data[list(self.cache_data.keys())[-2]]

    def get(self, key):
        """
            get method
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
