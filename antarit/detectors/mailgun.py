from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class MailgunTokenDetector(BaseDetector):
    name = "Mailgun Token"
    provider = "mailgun"
    keywords = ("mailgun", "email", "api key")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\bkey-[0-9a-fA-F]{32}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
