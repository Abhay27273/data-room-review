"""
Turns ExtractedFacts (+ optionally an LLM call for free-text claims that
aren't neatly tabular) into Claims with a provisional status.

TODO(you): start deterministic — a lot of claims (certificates listed vs
provided, numbers in spec sheets vs test reports) can be matched by
keyword/structure without an LLM at all. Reach for the model provider only
where you genuinely need language understanding (e.g. pulling a claim out
of a prose paragraph in the company overview).
"""

from ier.evidence.schema import Claim
from ier.ingestion.schema import ExtractedFact


class ClaimExtractor:
    def extract(self, facts: list[ExtractedFact]) -> list[Claim]:
        raise NotImplementedError
