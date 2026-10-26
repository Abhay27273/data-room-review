"""Orchestrates all checks against the rulebook + evidence register.

TODO(you): a CheckRunner that holds a list of Check instances, iterates
the rulebook's rules, finds every check that applies_to a given rule, and
collects CheckResults. A rule with no applicable check should surface as
CANT_CHECK, not silently disappear.
"""

from ier.checks.base import Check
from ier.checks.schema import CheckResult
from ier.evidence.register import EvidenceRegister
from ier.rulebook.schema import Rule


class CheckRunner:
    def __init__(self, checks: list[Check]):
        self.checks = checks

    def run_all(self, rules: list[Rule], register: EvidenceRegister) -> list[CheckResult]:
        raise NotImplementedError
