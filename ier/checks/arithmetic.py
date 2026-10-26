"""Arithmetic consistency inside a single document (e.g. a financial
model's totals actually add up, a spec sheet's derived figures are
consistent with its inputs).

TODO(you): implement ArithmeticCheck(Check).
"""

from ier.checks.base import Check


class ArithmeticCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError
