"""
Optional: a provider that talks to a locally served open-weight model
(e.g. via Ollama or vLLM's OpenAI-compatible endpoint). The brief notes
this is welcome but not required — build it last, and only if time
allows, since it adds serving/setup complexity.

TODO(you): if you build this, document in the README which model,
quantization, and serving setup you used, per the brief's request, so it
can be reproduced on other hardware.
"""

from ier.models.base import ModelProvider


class LocalProvider(ModelProvider):
    def __init__(self, base_url: str, model: str):
        self.base_url = base_url
        self.model = model

    def generate_structured(self, prompt, schema):
        raise NotImplementedError
