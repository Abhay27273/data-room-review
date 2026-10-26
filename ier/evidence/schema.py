"""
Core data shapes for the evidence register. Arguably the single most
important schema in the project.
"""

from dataclasses import dataclass, field
from enum import Enum

from ier.ingestion.schema import SourceLocation


class EvidenceStatus(str, Enum):
    """The four statuses every claim must be classified into.

    TODO(you): double check these match the wording the report format
    (once you have it) expects — the brief uses "documented", "asserted
    only", "contradicted", and "missing" (evidence the rulebook requires
    but the room lacks).
    """

    DOCUMENTED = "documented"
    ASSERTED_ONLY = "asserted_only"
    CONTRADICTED = "contradicted"
    MISSING = "missing"


class ClaimCategory(str, Enum):
    """TODO(you): refine against the rulebook once you have it — these are
    a first guess at the categories the brief lists."""

    TECHNOLOGY = "technology"
    PERFORMANCE = "performance"
    SAFETY_CERTIFICATION = "safety_certification"
    CONTRACT = "contract"
    WARRANTY = "warranty"
    IMPACT = "impact"


@dataclass(frozen=True)
class EvidenceRef:
    """A pointer from a claim to the exact place a source does or doesn't
    support it — this is what makes a citation checkable."""

    source: SourceLocation
    quote_or_value: str


@dataclass
class Claim:
    """One claim about the project, its current status, and the evidence
    (for or against) that produced that status.

    TODO(you): decide how a Claim's `asserted_by` (which document/where
    the company stated it) differs from `supporting_evidence` /
    `contradicting_evidence` (what a primary document shows) — keeping
    these separate is what lets you tell "asserted only" apart from
    "documented" and "contradicted".
    """

    id: str
    category: ClaimCategory
    statement: str
    status: EvidenceStatus
    asserted_by: list[EvidenceRef] = field(default_factory=list)
    supporting_evidence: list[EvidenceRef] = field(default_factory=list)
    contradicting_evidence: list[EvidenceRef] = field(default_factory=list)
    notes: str = ""
