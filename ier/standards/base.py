"""Interface for a source of external reference material, so the web
fetcher is swappable (and mockable in tests) without touching callers."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class StandardRef:
    """TODO(you): this is what gets cited for an external fact — keep url
    + date_read on every one, per the brief's "cite each with its URL and
    the date read" requirement.
    """

    url: str
    date_read: date
    content: str


class StandardsSource(ABC):
    @abstractmethod
    def fetch(self, url: str) -> StandardRef:
        raise NotImplementedError
