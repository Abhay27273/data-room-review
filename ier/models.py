from abc import ABC, abstractmethod
from typing import Type, TypeVar

import anthropic
from pydantic import BaseModel, ValidationError

T = TypeVar("T", bound=BaseModel)


class ModelProvider(ABC):
    @abstractmethod
    def generate_structured(self, prompt: str, schema: Type[T]) -> T:
        raise NotImplementedError


class AnthropicProvider(ModelProvider):
    def __init__(self, api_key: str, model: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model

    def generate_structured(self, prompt: str, schema: Type[T]) -> T:
        tool = {
            "name": "extract",
            "description": "Extract structured data matching the schema",
            "input_schema": schema.model_json_schema(),
        }

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            tools=[tool],
            tool_choice={"type": "tool", "name": "extract"},
            messages=[{"role": "user", "content": prompt}],
        )

        tool_use = next(block for block in response.content if block.type == "tool_use")
        return schema.model_validate(tool_use.input)


class OpenAiProvider(ModelProvider):
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def generate_structured(self, prompt, schema):
        raise NotImplementedError


class LocalProvider(ModelProvider):
    def __init__(self, base_url: str, model: str):
        self.base_url = base_url
        self.model = model

    def generate_structured(self, prompt, schema):
        raise NotImplementedError


def generate_validated(provider: ModelProvider, prompt: str, schema: Type[T], max_retries: int = 2) -> T:
    last_error = None
    for _ in range(max_retries + 1):
        try:
            return provider.generate_structured(prompt, schema)
        except (ValidationError, StopIteration) as e:
            last_error = e
    raise ValueError(f"model output failed schema validation after {max_retries} retries: {last_error}")
