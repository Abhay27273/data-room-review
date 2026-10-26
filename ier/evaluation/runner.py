"""
TODO(you): EvaluationRunner runs the full pipeline (ingestion -> evidence
-> checks -> impact claims -> report) against each labeled data room,
wraps it in a CostTracker, and aggregates ier.evaluation.metrics across all
rooms.
"""


class EvaluationRunner:
    def run(self, data_room_paths: list, labels_path) -> dict:
        raise NotImplementedError
