"""
Checks the qualitative/wording side of an impact claim: a carbon-only
claim that ignores a trade-off the documents show (water, air pollution,
materials); a comparative claim without a common product category rule or
independent review; generic "green" or offset-based "carbon neutral"
wording.

TODO(you): these likely need the model provider (free-text claims, not
tabular data) — route through ier.models.retry.generate_validated rather
than calling a provider directly, so they get schema-checking for free.
"""


def check_ignored_tradeoffs(claim, register):
    raise NotImplementedError


def check_comparative_claim_basis(claim, register):
    raise NotImplementedError


def check_generic_green_wording(claim, register):
    raise NotImplementedError
