from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class GeminiDetector(BaseDetector):
    name = "Gemini API Key"
    provider = "gemini"
    keywords = ("gemini", "bard", "google ai", "api key")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"(?i)gemini_api_key[\"'=:\\s]{0,5}([A-Za-z0-9_\-]{20,})"),
            re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
