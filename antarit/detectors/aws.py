from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class AWSAccessKeyDetector(BaseDetector):
    name = "AWS Access Key"
    provider = "aws"
    keywords = ("aws", "access key", "secret key", "iam", "session")

    def compile_patterns(self) -> List[Pattern[str]]:
        # AKIA/ASIA prefixes are common for AWS access keys and temporary session keys.
        return [
            re.compile(r"\b(AKIA|ASIA)[0-9A-Z]{16}\b"),
            re.compile(r"(?i)aws_secret_access_key[\"'=:\\s]{0,5}([A-Za-z0-9/+=]{40})"),
            re.compile(r"(?i)aws_session_token[\"'=:\\s]{0,5}([A-Za-z0-9/+=]{80,})"),
        ]

    def provider_name(self) -> str:
        return self.provider
