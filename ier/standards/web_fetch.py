"""
TODO(you): implement WebStandardsSource(StandardsSource). Check the cache
(cache.py) before making a request, and write through to it after a
successful fetch, so a run can be repeated without re-hitting the network
— per the brief's "cache what you fetch so a run can be repeated".
"""

from ier.standards.base import StandardsSource
from ier.standards.cache import FileCache


class WebStandardsSource(StandardsSource):
    def __init__(self, cache: FileCache):
        self.cache = cache

    def fetch(self, url):
        raise NotImplementedError
