#!/usr/bin/python3
"""
    LIFO Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
        LIFOCache
    """
    def __init__(self):
        """
            init method
        """
        super().__init__()

    def put(self, key, item):
        """
            put method
        """
        if not (key and item):
            return None
        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item
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
            return self.cache_data[key]
