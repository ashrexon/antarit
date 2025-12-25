from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class TravisCITokenDetector(BaseDetector):
    name = "Travis CI Token"
    provider = "travisci"
    keywords = ("travis", "ci", "token", "api")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"(?i)travis[_-]?api[_-]?token[\"'=:\\s]{0,5}([0-9a-f]{40})"),
        ]

    def provider_name(self) -> str:
        return self.provider
