from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class RedisDetector(BaseDetector):
    name = "Redis URI"
    provider = "redis"
    keywords = ("redis", "cache", "uri")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"redis:\/\/:[^\/\s@]+@[^\/\s]+"),
        ]

    def provider_name(self) -> str:
        return self.provider
