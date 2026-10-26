"""Claimed uptime/performance vs the operating data actually recorded.

TODO(you): implement PerformanceVsOperatingCheck(Check).
"""

from ier.checks.base import Check


class PerformanceVsOperatingCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError
