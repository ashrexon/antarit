from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class GoogleAIDetector(BaseDetector):
    name = "Google AI API Key"
    provider = "googleai"
    keywords = ("google ai", "vertex", "ai", "generative", "gemini", "api key")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b"),
            re.compile(r"(?i)google_ai_api_key[\"'=:\\s]{0,5}([A-Za-z0-9_\-]{20,})"),
        ]

    def provider_name(self) -> str:
        return self.provider
