from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class VaultTokenDetector(BaseDetector):
    name = "Vault Token"
    provider = "vault"
    keywords = ("vault", "hashicorp", "hvac", "token")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\b(?:s|hvs)\.[A-Za-z0-9]{20,}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
