from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class MongoDBDetector(BaseDetector):
    name = "MongoDB URI"
    provider = "mongodb"
    keywords = ("mongodb", "mongo", "database", "uri")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"mongodb(?:\+srv)?:\/\/[^\/\s:@]+:[^\/\s:@]+@[^\/\s]+"),
        ]

    def provider_name(self) -> str:
        return self.provider
