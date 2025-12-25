from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class JenkinsTokenDetector(BaseDetector):
    name = "Jenkins API Token"
    provider = "jenkins"
    keywords = ("jenkins", "api token", "jenkins_token")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"(?i)jenkins[_-]?api[_-]?token[\"'=:\\s]{0,5}([A-Za-z0-9]{24,})"),
        ]

    def provider_name(self) -> str:
        return self.provider
