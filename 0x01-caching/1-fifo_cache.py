#!/usr/bin/python3
"""
    FIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        fifo caching
    """

    def __init__(self):
        """
            init function
        """
        super().__init__()

    def put(self, key, item):
        """
            put function
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
                theKey = list(self.cache_data.keys())[0]
                self.cache_data.pop(theKey)
                print('DISCARD ' + theKey)

    def get(self, key):
        """
            get function
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]