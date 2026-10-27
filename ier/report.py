from dataclasses import dataclass, field

from ier.checks import CheckResult
from ier.evidence import EvidenceRegister
from ier.impact_claims import ImpactClaimResult


@dataclass
class Finding:
    title: str
    severity: str
    evidence: list = field(default_factory=list)
    resolution: str = ""


@dataclass
class Report:
    scope_and_documents: str = ""
    technical_review: str = ""
    commercial_review: str = ""
    risk_and_safety: str = ""
    impact_claims_section: str = ""
    findings: list[Finding] = field(default_factory=list)
    questions_for_company: list[str] = field(default_factory=list)
    readiness_view: str = ""


def build_report(register: EvidenceRegister, check_results: list[CheckResult],
                  impact_results: list[ImpactClaimResult], readiness) -> Report:
    raise NotImplementedError


def render_markdown(report: Report) -> str:
    raise NotImplementedError
