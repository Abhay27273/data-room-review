import json
from dataclasses import asdict, dataclass, field
from enum import Enum

from ier.ingestion import ExtractedFact, SourceLocation


class EvidenceStatus(str, Enum):
    DOCUMENTED = "documented"
    ASSERTED_ONLY = "asserted_only"
    CONTRADICTED = "contradicted"
    MISSING = "missing"


class ClaimCategory(str, Enum):
    TECHNOLOGY = "technology"
    PERFORMANCE = "performance"
    SAFETY_CERTIFICATION = "safety_certification"
    CONTRACT = "contract"
    WARRANTY = "warranty"
    IMPACT = "impact"


@dataclass(frozen=True)
class EvidenceRef:
    source: SourceLocation
    quote_or_value: str


@dataclass
class Claim:
    id: str
    category: ClaimCategory
    statement: str
    status: EvidenceStatus
    asserted_by: list[EvidenceRef] = field(default_factory=list)
    supporting_evidence: list[EvidenceRef] = field(default_factory=list)
    contradicting_evidence: list[EvidenceRef] = field(default_factory=list)
    notes: str = ""


class EvidenceRegister:
    def __init__(self):
        self._claims: dict[str, Claim] = {}

    def add(self, claim: Claim) -> None:
        if claim.id in self._claims:
            raise ValueError(f"duplicate claim id: {claim.id}")
        self._claims[claim.id] = claim

    def by_category(self, category: ClaimCategory) -> list[Claim]:
        return [c for c in self._claims.values() if c.category == category]

    def by_status(self, status: EvidenceStatus) -> list[Claim]:
        return [c for c in self._claims.values() if c.status == status]

    def to_json(self) -> str:
        return json.dumps([asdict(c) for c in self._claims.values()], indent=2)


class ClaimExtractor:
    def extract(self, facts: list[ExtractedFact]) -> list[Claim]:
        raise NotImplementedError
