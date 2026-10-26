"""
Wraps any ModelProvider call with schema validation + retry, so every call
site gets "every model output passes a schema check before it is used;
failures are retried or flagged" for free instead of reimplementing it per
call site.
"""

from typing import Type, TypeVar

from pydantic import BaseModel

from ier.models.base import ModelProvider

T = TypeVar("T", bound=BaseModel)


def generate_validated(
    provider: ModelProvider,
    prompt: str,
    schema: Type[T],
    max_retries: int = 2,
) -> T:
    """Call provider.generate_structured, retrying on a schema validation
    failure up to max_retries times.

    TODO(you): on final failure, don't raise and silently drop the fact —
    return/raise something the caller can turn into a "flagged, needs
    human review" entry rather than losing the finding entirely.
    """
    raise NotImplementedError
