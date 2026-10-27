import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    data_root: Path
    cache_root: Path
    output_root: Path
    anthropic_api_key: Optional[str]
    anthropic_model: str


def load() -> Settings:
    return Settings(
        data_root=Path(os.getenv("IER_DATA_ROOT", "./data/provided")),
        cache_root=Path(os.getenv("IER_CACHE_ROOT", "./cache")),
        output_root=Path(os.getenv("IER_OUTPUT_ROOT", "./outputs")),
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
        anthropic_model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5"),
    )
