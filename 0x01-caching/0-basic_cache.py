#!/usr/bin/python3
"""
    Basic dictionary
"""

BaseCashing = __import__('base_caching').BaseCaching


class BasicCache(BaseCashing):
    """
        Basic dictionary
    """

    def put(self, key, item):
        """
            put data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
            get data
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
