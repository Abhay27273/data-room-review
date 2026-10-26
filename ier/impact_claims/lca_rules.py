"""
Checks against the quantitative/methodological side of a life-cycle claim:
functional unit, boundary, cut-off, grid-factor basis, measured vs
nameplate power, lifetime assumptions, baseline for a "% reduction",
activity- vs spend-based emission factors.

TODO(you): one function per rule element, each returning whether the
claim's supporting document states it and what it says, so lca_rules and
wording_checks can be combined into one ImpactClaimResult per claim.
"""


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
