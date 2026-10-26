"""Runs every lca_rules + wording_checks function over each impact claim
and combines the results into one ImpactClaimResult per claim.

TODO(you): implement ImpactClaimsRunner.
"""

from ier.evidence.register import EvidenceRegister
from ier.impact_claims.schema import ImpactClaimResult


class ImpactClaimsRunner:
    def run_all(self, register: EvidenceRegister) -> list[ImpactClaimResult]:
        raise NotImplementedError
