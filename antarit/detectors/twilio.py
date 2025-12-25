from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class TwilioTokenDetector(BaseDetector):
    name = "Twilio Credentials"
    provider = "twilio"
    keywords = ("twilio", "sid", "auth token")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\bAC[0-9a-fA-F]{32}\b"),
            re.compile(r"\bSK[0-9a-fA-F]{32}\b"),
            re.compile(r"(?i)twilio_auth_token[\"'=:\\s]{0,5}([0-9a-f]{32})"),
        ]

    def provider_name(self) -> str:
        return self.provider
