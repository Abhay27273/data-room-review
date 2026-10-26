"""
In-memory store for the evidence register built from one data room, plus
whatever (de)serialization the report/evaluation stages need.

TODO(you): add / by_category / by_status, and a way to export the whole
register (JSON is probably easiest, and gives you something diffable
against the evaluation labels).
"""

from ier.evidence.schema import Claim, ClaimCategory, EvidenceStatus


class EvidenceRegister:
    def __init__(self):
        self._claims: list[Claim] = []

    def add(self, claim: Claim) -> None:
        raise NotImplementedError

    def by_category(self, category: ClaimCategory) -> list[Claim]:
        raise NotImplementedError

    def by_status(self, status: EvidenceStatus) -> list[Claim]:
        raise NotImplementedError

    def to_json(self) -> str:
        raise NotImplementedError
