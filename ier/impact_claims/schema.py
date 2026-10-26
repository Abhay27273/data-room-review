from dataclasses import dataclass, field
from enum import Enum

from ier.evidence.schema import EvidenceRef


class ImpactVerdict(str, Enum):
    SUPPORTED = "supported"
    UNSUPPORTED = "unsupported"
    CONTRADICTED = "contradicted"


@dataclass
class ImpactClaimResult:
    """TODO(you): `issues` should name which specific life-cycle-rule
    element is missing/wrong (functional unit, boundary, cut-off,
    grid-factor basis, measured-vs-nameplate power, lifetime assumption,
    missing baseline, activity- vs spend-based factors, an ignored
    trade-off, an unsupported comparative claim, generic "green"/offset
    wording) — a bare SUPPORTED/UNSUPPORTED isn't actionable on its own.
    """

    claim_id: str
    verdict: ImpactVerdict
    issues: list[str] = field(default_factory=list)
    evidence: list[EvidenceRef] = field(default_factory=list)
