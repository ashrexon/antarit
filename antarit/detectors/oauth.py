from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class OAuthTokenDetector(BaseDetector):
    name = "OAuth Bearer Token"
    provider = "oauth"
    keywords = ("oauth", "bearer", "auth", "authorization")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"(?i)bearer\s+([A-Za-z0-9._\-]{32,})"),
            re.compile(r"(?i)basic\s+([A-Za-z0-9+/=]{16,})"),
        ]

    def provider_name(self) -> str:
        return self.provider
