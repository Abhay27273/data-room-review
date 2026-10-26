"""Result shape every check function returns, independent of which check
produced it — this is what the report's "findings" section is built
from."""

from dataclasses import dataclass, field
from enum import Enum

from ier.evidence.schema import EvidenceRef


class CheckStatus(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    CANT_CHECK = "cant_check"


@dataclass
class CheckResult:
    """TODO(you): a fail result needs the actual values on both sides of
    the comparison (not just "mismatch") so the report can show, e.g.,
    "contract requires 4h duration; after degradation the system delivers
    3.6h" with sources for both numbers — see the brief's acceptance
    criterion that contract/warranty calculations are correct and cited.
    """

    rule_id: str
    status: CheckStatus
    evidence: list[EvidenceRef] = field(default_factory=list)
    explanation: str = ""
    severity: str = ""
