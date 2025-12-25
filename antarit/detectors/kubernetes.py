from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class KubernetesDetector(BaseDetector):
    name = "Kubernetes Secret"
    provider = "kubernetes"
    keywords = ("kubeconfig", "kubernetes", "cluster", "token")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"(?i)token:\s*([A-Za-z0-9._\-]{20,})"),
            re.compile(r'(?i)"client-certificate-data"\s*:\s*"([A-Za-z0-9+/=]{32,})"'),
        ]

    def provider_name(self) -> str:
        return self.provider
