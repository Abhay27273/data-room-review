"""Modelled (financial model / forecast) results vs actual operating
results.

TODO(you): implement ModelledVsActualCheck(Check).
"""

from ier.checks.base import Check


class ModelledVsActualCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError
