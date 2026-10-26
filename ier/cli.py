"""
Command-line entry point.

TODO(you): wire up two subcommands with click or argparse:
  - `run`      : process one data room end-to-end -> evidence register,
                 check results, impact-claim results, report.
  - `evaluate` : run `run` across the labeled test data rooms and print
                 the evaluation metrics from ier.evaluation.metrics.

Keep this file thin — it should only parse args and call into the
pipeline modules, not contain any parsing/checking logic itself.
"""


def main() -> None:
    """Entry point, invoked as `python -m ier.cli`."""
    raise NotImplementedError
