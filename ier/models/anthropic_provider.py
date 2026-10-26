"""
TODO(you): implement AnthropicProvider(ModelProvider) using the `anthropic`
SDK. Use tool-calling / structured output so the model's response maps
directly onto the pydantic schema passed to generate_structured, rather
than parsing free text.
"""

from ier.models.base import ModelProvider


class AnthropicProvider(ModelProvider):
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def generate_structured(self, prompt, schema):
        raise NotImplementedError
