"""
TODO(you): a small context-manager-friendly tracker that records
wall-clock time and (if using a paid API) token usage/cost for a single
data-room run, per the brief's "time and cost per data room" requirement.
"""


class CostTracker:
    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, *exc):
        raise NotImplementedError

    def record_model_call(self, provider_name: str, input_tokens: int, output_tokens: int) -> None:
        raise NotImplementedError
