import time
from typing import Optional


def findings_recall(found_findings: list[str], labeled_planted_issues: list[str]) -> float:
    if not labeled_planted_issues:
        return 1.0
    found = set(found_findings)
    return sum(1 for issue in labeled_planted_issues if issue in found) / len(labeled_planted_issues)


def false_alarm_rate(found_findings: list[str], labeled_planted_issues: list[str]) -> float:
    if not found_findings:
        return 0.0
    labeled = set(labeled_planted_issues)
    false_alarms = sum(1 for finding in found_findings if finding not in labeled)
    return false_alarms / len(found_findings)


def status_accuracy(predicted_claims: dict[str, str], labeled_claims: dict[str, str]) -> float:
    if not labeled_claims:
        return 1.0
    correct = sum(1 for claim_id, status in labeled_claims.items() if predicted_claims.get(claim_id) == status)
    return correct / len(labeled_claims)


def citation_accuracy(predicted_claims: dict, labeled_claims: dict) -> float:
    raise NotImplementedError


def calculation_error_rate(check_results: list, labeled_check_results: list) -> float:
    raise NotImplementedError


class CostTracker:
    def __init__(self):
        self.input_tokens = 0
        self.output_tokens = 0
        self.start_time: Optional[float] = None
        self.elapsed_seconds: Optional[float] = None

    def __enter__(self):
        self.start_time = time.monotonic()
        return self

    def __exit__(self, *exc):
        self.elapsed_seconds = time.monotonic() - self.start_time

    def record_model_call(self, provider_name: str, input_tokens: int, output_tokens: int) -> None:
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens


class EvaluationRunner:
    def run(self, data_room_paths: list, labels_path) -> dict:
        raise NotImplementedError
