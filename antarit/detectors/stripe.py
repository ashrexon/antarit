from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class StripeKeyDetector(BaseDetector):
    name = "Stripe Key"
    provider = "stripe"
    keywords = ("stripe", "payment", "secret", "sk_live", "sk_test")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\bsk_live_[0-9a-zA-Z]{24,}\b"),
            re.compile(r"\bsk_test_[0-9a-zA-Z]{24,}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
