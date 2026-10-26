"""
The interface every model provider implements. Every call that goes
through this interface returns data that will be schema-checked before
use — this file stays provider-agnostic so the schema-check/retry logic
in retry.py doesn't need to know which provider ran.
"""

from abc import ABC, abstractmethod
from typing import Type, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class ModelProvider(ABC):
    """Generates a structured response conforming to a pydantic schema."""

    @abstractmethod
    def generate_structured(self, prompt: str, schema: Type[T]) -> T:
        """Call the model and parse its response into `schema`.

        TODO(you): the implementation should NOT silently swallow a
        response that doesn't match the schema — let retry.py's wrapper
        handle that, per the "every model output passes a schema check
        before it is used" requirement.
        """
        raise NotImplementedError
