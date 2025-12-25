from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class SlackTokenDetector(BaseDetector):
    name = "Slack Token"
    provider = "slack"
    keywords = ("slack", "xoxb", "xoxp", "bot")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{10,48}\b"),
        ]

    def provider_name(self) -> str:
        return self.provider
