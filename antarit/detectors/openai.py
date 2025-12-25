from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class OpenAIDetector(BaseDetector):
    name = "OpenAI API Key"
    provider = "openai"
    keywords = ("openai", "gpt", "sk-", "api key")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
                re.compile(r"\bsk-[A-Za-z0-9]{32,64}\b")
        ]

    def provider_name(self) -> str:
        return self.provider
