"""
TODO(you): score_criterion should score one lender criterion (derived from
the published standards, per the brief) as 0, 0.5, or 1 with its
supporting evidence, or "not_assessable" when the room doesn't have what's
needed to judge it.
"""

from typing import Literal

Score = Literal[0, 0.5, 1, "not_assessable"]


def score_criterion(criterion_id: str, register) -> tuple[Score, list]:
    raise NotImplementedError
