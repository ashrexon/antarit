from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class AzureDetector(BaseDetector):
    name = "Azure Credentials"
    provider = "azure"
    keywords = ("azure", "client secret", "tenant", "storage", "microsoft")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"(?i)azure_storage_key[\"'=:\\s]{0,5}([A-Za-z0-9+/]{86,88}={0,2})"),
            re.compile(r"(?i)azure_client_secret[\"'=:\\s]{0,5}([A-Za-z0-9._~+-]{20,})"),
            re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b.*\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
