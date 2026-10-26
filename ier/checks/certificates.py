"""Certificates claimed (in the company overview / spec sheets) vs
certificates actually provided (as certificate documents in the room).

TODO(you): implement CertificatesCheck(Check).
"""

from ier.checks.base import Check


class CertificatesCheck(Check):
    def applies_to(self, rule):
        raise NotImplementedError

    def run(self, rule, register):
        raise NotImplementedError
