from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum

from ier.evidence import EvidenceRef, EvidenceRegister
from ier.rulebook import Rule


class CheckStatus(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    CANT_CHECK = "cant_check"


@dataclass
class CheckResult:
    rule_id: str
    status: CheckStatus
    evidence: list[EvidenceRef] = field(default_factory=list)
    explanation: str = ""
    severity: str = ""


class Check(ABC):
    @abstractmethod
    def applies_to(self, rule: Rule) -> bool:
        raise NotImplementedError

    @abstractmethod
    def run(self, rule: Rule, register: EvidenceRegister) -> CheckResult:
        raise NotImplementedError


class CertificatesCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError


class SpecVsTestCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError


class PerformanceVsOperatingCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError


class ModelledVsActualCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError


class ContractObligationsCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError


class WarrantyTermsCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError


class ArithmeticCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError


class CheckRunner:
    def __init__(self, checks: list[Check]):
        self.checks = checks

    def run_all(self, rules: list[Rule], register: EvidenceRegister) -> list[CheckResult]:
        raise NotImplementedError
