"""
TODO(you): classify_risk_model should read the evidence register (revenue
contracts present? tariff/market exposure? regulated return?) and return
one of the three business-risk models, with the evidence it based the
classification on — not just a bare label.
"""

from typing import Literal

from ier.evidence.register import EvidenceRegister

RiskModel = Literal["contracted", "merchant", "regulated"]


def classify_risk_model(register: EvidenceRegister) -> tuple[RiskModel, list]:
    raise NotImplementedError
