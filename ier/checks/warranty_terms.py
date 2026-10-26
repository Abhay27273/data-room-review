"""Warranty terms (period, throughput limits, capacity adjustments) vs the
planned duty cycle.

TODO(you): implement WarrantyTermsCheck(Check). See the note in
contract_obligations.py about calculation correctness — the same applies
here.
"""

from ier.checks.base import Check


class WarrantyTermsCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError
