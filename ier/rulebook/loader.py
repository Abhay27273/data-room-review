"""
TODO(you): implement load_rulebook once you know the provided file format
(likely YAML/JSON/CSV). Fail loudly on a malformed rule rather than
silently skipping it — a dropped rule is a silently-missed check.
"""

from pathlib import Path

from ier.rulebook.schema import Rule


def load_rulebook(path: Path) -> list[Rule]:
    raise NotImplementedError
