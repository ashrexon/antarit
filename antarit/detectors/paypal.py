from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class PayPalDetector(BaseDetector):
    name = "PayPal Credentials"
    provider = "paypal"
    keywords = ("paypal", "client id", "client secret")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"(?i)paypal_client_id[\"'=:\\s]{0,5}([A-Za-z0-9]{20,})"),
            re.compile(r"(?i)paypal_secret[\"'=:\\s]{0,5}([A-Za-z0-9]{32,})"),
        ]

    def provider_name(self) -> str:
        return self.provider
