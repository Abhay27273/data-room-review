"""
Central place for paths and settings the rest of the tool reads from.

TODO(you): load environment variables (see .env.example) with
python-dotenv, resolve the data/cache/output roots below, and expose them
as a single Settings object that other modules import instead of
hardcoding paths.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Settings:
    """Resolved runtime configuration.

    TODO(you): fill in the fields you actually need (data room path,
    rulebook path, standards/report-format paths, cache dir, output dir,
    model provider name + API key, etc.) and a `load() -> Settings`
    function that builds one from environment variables + CLI overrides.
    """

    data_root: Path
    cache_root: Path
    output_root: Path
