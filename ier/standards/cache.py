"""Local cache for fetched standards, keyed by URL.

TODO(you): get(url) -> StandardRef | None, set(url, ref) -> None, backed
by files under the cache/ directory (see ier/config.py).
"""

from typing import Optional

from ier.standards.base import StandardRef


class FileCache:
    def __init__(self, root):
        self.root = root

    def get(self, url: str) -> Optional[StandardRef]:
        raise NotImplementedError

    def set(self, url: str, ref: StandardRef) -> None:
        raise NotImplementedError
