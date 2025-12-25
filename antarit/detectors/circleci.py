from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class CircleCITokenDetector(BaseDetector):
    name = "CircleCI Token"
    provider = "circleci"
    keywords = ("circleci", "ci", "token", "api")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"(?i)circleci_token[\"'=:\\s]{0,5}([0-9a-f]{40})"),
            re.compile(r"\bCIRCLECI_[A-Z0-9_]*TOKEN[\"'=:\\s]{0,5}([A-Za-z0-9]{32,})"),
        ]

    def provider_name(self) -> str:
        return self.provider
