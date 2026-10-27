from dataclasses import dataclass, field
from enum import Enum

from ier.evidence import EvidenceRef, EvidenceRegister


class ImpactVerdict(str, Enum):
    SUPPORTED = "supported"
    UNSUPPORTED = "unsupported"
    CONTRADICTED = "contradicted"


@dataclass
class ImpactClaimResult:
    claim_id: str
    verdict: ImpactVerdict
    issues: list[str] = field(default_factory=list)
    evidence: list[EvidenceRef] = field(default_factory=list)


def check_functional_unit(claim, register):
    raise NotImplementedError


def check_boundary_and_cutoff(claim, register):
    raise NotImplementedError


def check_grid_factor_basis(claim, register):
    raise NotImplementedError


def check_measured_vs_nameplate(claim, register):
    raise NotImplementedError


def check_baseline_for_reduction_claim(claim, register):
    raise NotImplementedError


def check_emission_factor_basis(claim, register):
    raise NotImplementedError


def check_ignored_tradeoffs(claim, register):
    raise NotImplementedError


def check_comparative_claim_basis(claim, register):
    raise NotImplementedError


def check_generic_green_wording(claim, register):
    raise NotImplementedError


class ImpactClaimsRunner:
    def run_all(self, register: EvidenceRegister) -> list[ImpactClaimResult]:
        raise NotImplementedError
