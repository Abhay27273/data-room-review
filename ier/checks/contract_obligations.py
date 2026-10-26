"""Contract obligations (dispatch duration, availability, penalty tiers,
payment thresholds) vs what the system can actually deliver after
degradation.

TODO(you): implement ContractObligationsCheck(Check). This is one of the
two check types the brief explicitly requires to be numerically correct
("contract and warranty calculations are correct") — write the arithmetic
carefully and unit-test it with a few hand-checked examples before
trusting it on real data.
"""

from ier.checks.base import Check


class ContractObligationsCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError
