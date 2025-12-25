from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class BitbucketTokenDetector(BaseDetector):
    name = "Bitbucket Token"
    provider = "bitbucket"
    keywords = ("bitbucket", "oauth", "app password", "bb")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"(?i)bitbucket[_A-Z]*token[\"'=:\\s]{0,5}([A-Za-z0-9]{32,})"),
            re.compile(r"(?i)bitbucket_password[\"'=:\\s]{0,5}([A-Za-z0-9!@#$%^&*()_+=\\-]{12,})"),
        ]

    def provider_name(self) -> str:
        return self.provider
