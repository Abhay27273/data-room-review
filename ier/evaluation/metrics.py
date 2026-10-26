"""
TODO(you): one function per metric the brief asks for. Each should take
the tool's output + the provided labels for one room and return a number
(or a small structured result showing which planted issues were
found/missed, which is more useful for debugging than a bare score).
"""


def findings_recall(found_findings, labeled_planted_issues) -> float:
    raise NotImplementedError


def false_alarm_rate(found_findings, labeled_planted_issues) -> float:
    raise NotImplementedError


def status_accuracy(predicted_claims, labeled_claims) -> float:
    raise NotImplementedError


def citation_accuracy(predicted_claims, labeled_claims) -> float:
    raise NotImplementedError


def calculation_error_rate(check_results, labeled_check_results) -> float:
    raise NotImplementedError
