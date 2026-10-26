"""
TODO(you): replace this with the real structure once you have the provided
report format. Placeholder sections per the brief: scope and documents
reviewed; technical review; commercial review; risk and safety; impact
claims; findings ranked by severity (each with evidence + what would
resolve it); questions for the company; readiness view.
"""

from dataclasses import dataclass, field


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
