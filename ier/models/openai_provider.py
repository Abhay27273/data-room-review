"""
Optional second provider, to demonstrate the interface is actually
swappable. Build this after AnthropicProvider works end-to-end, not before.

TODO(you): implement OpenAiProvider(ModelProvider) the same way as
AnthropicProvider, using OpenAI's structured-output / function-calling
support.
"""

from ier.models.base import ModelProvider


class OpenAiProvider(ModelProvider):
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def generate_structured(self, prompt, schema):
        raise NotImplementedError
