from typing import Literal

from ier.evidence import EvidenceRegister

RiskModel = Literal["contracted", "merchant", "regulated"]
Score = Literal[0, 0.5, 1, "not_assessable"]


def classify_risk_model(register: EvidenceRegister) -> tuple[RiskModel, list]:
    raise NotImplementedError


def score_criterion(criterion_id: str, register: EvidenceRegister) -> tuple[Score, list]:
    raise NotImplementedError
