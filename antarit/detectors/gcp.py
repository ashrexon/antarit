from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class GCPDetector(BaseDetector):
    name = "GCP API Key"
    provider = "gcp"
    keywords = ("gcp", "google", "api key", "firebase", "gcloud")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            # Typical GCP API key format.
            re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b"),
            # Service account private key block.
            re.compile(r"-----BEGIN PRIVATE KEY-----"),
        ]

    def provider_name(self) -> str:
        return self.provider
