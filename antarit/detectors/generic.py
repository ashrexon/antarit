from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class GenericEntropyDetector(BaseDetector):
    name = "Generic High Entropy"
    provider = "generic"
    keywords = ("secret", "token", "key", "password", "auth")

    def compile_patterns(self) -> List[Pattern[str]]:
        # Broad pattern for opaque tokens; entropy validator will filter false positives.
        return [
            re.compile(r"\b[A-Za-z0-9_\-]{24,}\b"),
            re.compile(r"\b[A-Za-z0-9/\+=]{24,}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
