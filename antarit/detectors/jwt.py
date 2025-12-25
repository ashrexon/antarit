from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class JWTDetector(BaseDetector):
    name = "JWT"
    provider = "jwt"
    keywords = ("jwt", "token", "authorization", "bearer")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
