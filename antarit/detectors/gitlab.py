from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class GitLabTokenDetector(BaseDetector):
    name = "GitLab Token"
    provider = "gitlab"
    keywords = ("gitlab", "glpat", "token", "ci")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\bglpat-[0-9A-Za-z_-]{20,}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
