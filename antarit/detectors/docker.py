from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class DockerDetector(BaseDetector):
    name = "Docker Credential"
    provider = "docker"
    keywords = ("docker", "registry", "auth")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r'"auth"\s*:\s*"([A-Za-z0-9+/=]{16,})"'),
        ]

    def provider_name(self) -> str:
        return self.provider
