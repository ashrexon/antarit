from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class FirebaseDetector(BaseDetector):
    name = "Firebase Key"
    provider = "firebase"
    keywords = ("firebase", "fcm", "google")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\bAAAA[A-Za-z0-9_-]{7,}\:[A-Za-z0-9_-]{140,}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
