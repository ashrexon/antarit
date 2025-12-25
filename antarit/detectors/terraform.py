from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class TerraformDetector(BaseDetector):
    name = "Terraform Secrets"
    provider = "terraform"
    keywords = ("terraform", "tfvars", "variable", "secret")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r'(?i)variable\s+"[A-Za-z0-9_]*secret"\s*\{\s*default\s*=\s*"([^"]{12,})"'),
            re.compile(r'(?i)secret\s*=\s*"([^"]{12,})"'),
        ]

    def provider_name(self) -> str:
        return self.provider
