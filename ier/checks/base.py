"""Interface every individual check implements, so the runner can treat
them uniformly regardless of what they compare."""

from abc import ABC, abstractmethod

from ier.checks.schema import CheckResult
from ier.evidence.register import EvidenceRegister
from ier.rulebook.schema import Rule


class Check(ABC):
    @abstractmethod
    def applies_to(self, rule: Rule) -> bool:
        """Whether this check knows how to evaluate the given rule."""
        raise NotImplementedError

    @abstractmethod
    def run(self, rule: Rule, register: EvidenceRegister) -> CheckResult:
        raise NotImplementedError
