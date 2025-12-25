from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class MySQLDetector(BaseDetector):
    name = "MySQL URI"
    provider = "mysql"
    keywords = ("mysql", "database", "uri")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"mysql:\/\/[^\/\s:@]+:[^\/\s:@]+@[^\/\s]+"),
        ]

    def provider_name(self) -> str:
        return self.provider
