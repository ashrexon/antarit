from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class SendGridTokenDetector(BaseDetector):
    name = "SendGrid Token"
    provider = "sendgrid"
    keywords = ("sendgrid", "sg.", "email", "api key")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\bSG\.[A-Za-z0-9_-]{16,}\.[A-Za-z0-9_-]{30,}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
