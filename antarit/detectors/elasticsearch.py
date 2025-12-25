from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class ElasticsearchDetector(BaseDetector):
    name = "Elasticsearch URI"
    provider = "elasticsearch"
    keywords = ("elastic", "elasticsearch", "es", "search")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"https?:\/\/[^\/\s:@]+:[^\/\s:@]+@[^\/\s]+:?[0-9]*"),
        ]

    def provider_name(self) -> str:
        return self.provider
