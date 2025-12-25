from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class GithubTokenDetector(BaseDetector):
    name = "GitHub Token"
    provider = "github"
    keywords = ("github", "ghp", "token", "gho", "oauth")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\bghp_[A-Za-z0-9]{36}\b"),
            re.compile(r"\bgithub_pat_[0-9A-Za-z_]{80,}\b"),
            re.compile(r"\bgho_[A-Za-z0-9]{36}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
