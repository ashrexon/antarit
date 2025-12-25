from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class RazorpayDetector(BaseDetector):
    name = "Razorpay Key"
    provider = "razorpay"
    keywords = ("razorpay", "rzp", "payment", "india")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\brzp_(live|test)_[A-Za-z0-9]{7,}\b"),
            re.compile(r"(?i)razorpay_key_secret[\"'=:\\s]{0,5}([A-Za-z0-9]{20,})"),
        ]

    def provider_name(self) -> str:
        return self.provider
