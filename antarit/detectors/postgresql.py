from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class PostgresDetector(BaseDetector):
    name = "PostgreSQL URI"
    provider = "postgresql"
    keywords = ("postgres", "postgresql", "database", "uri")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"postgres(?:ql)?:\/\/[^\/\s:@]+:[^\/\s:@]+@[^\/\s]+"),
        ]

    def provider_name(self) -> str:
        return self.provider
