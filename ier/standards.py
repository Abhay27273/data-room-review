import hashlib
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Optional

import requests


@dataclass(frozen=True)
class StandardRef:
    url: str
    date_read: date
    content: str


class StandardsSource(ABC):
    @abstractmethod
    def fetch(self, url: str) -> StandardRef:
        raise NotImplementedError


class FileCache:
    def __init__(self, root: Path):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path_for(self, url: str) -> Path:
        key = hashlib.sha256(url.encode()).hexdigest()
        return self.root / f"{key}.json"

    def get(self, url: str) -> Optional[StandardRef]:
        path = self._path_for(url)
        if not path.exists():
            return None
        data = json.loads(path.read_text())
        return StandardRef(url=data["url"], date_read=date.fromisoformat(data["date_read"]), content=data["content"])

    def set(self, url: str, ref: StandardRef) -> None:
        path = self._path_for(url)
        path.write_text(json.dumps({"url": ref.url, "date_read": ref.date_read.isoformat(), "content": ref.content}))


class WebStandardsSource(StandardsSource):
    def __init__(self, cache: FileCache):
        self.cache = cache

    def fetch(self, url: str) -> StandardRef:
        cached = self.cache.get(url)
        if cached is not None:
            return cached

        response = requests.get(url, timeout=30)
        response.raise_for_status()
        ref = StandardRef(url=url, date_read=date.today(), content=response.text)
        self.cache.set(url, ref)
        return ref
