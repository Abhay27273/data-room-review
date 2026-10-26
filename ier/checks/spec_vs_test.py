"""Rated/nameplate specs vs independent test-report data.

TODO(you): implement SpecVsTestCheck(Check). Watch units here — rated
power (kW) vs measured energy (kWh) over a test duration is a classic
place for a claim to look consistent when it isn't.
"""

from ier.checks.base import Check


class SpecVsTestCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError
