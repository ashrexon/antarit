from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Pattern


@dataclass
class Finding:
    file_path: Path
    line_number: int
    detector: str
    provider: str
    secret: str
    entropy: float | None = None
    line_preview: str | None = None
    confidence: str | None = None


class BaseDetector(ABC):
    name: str
    provider: str
    patterns: List[Pattern[str]]
    keywords: tuple[str, ...]

    def __init__(self) -> None:
        self.patterns = self.compile_patterns()

    @abstractmethod
    def compile_patterns(self) -> List[Pattern[str]]:
        """Return compiled regex patterns used by the detector."""

    @abstractmethod
    def provider_name(self) -> str:
        """Return provider identifier for filtering and reporting."""

    def detect(self, file_path: Path, content: str) -> list[Finding]:
        """Run detector against file content and return findings."""
        findings: list[Finding] = []
        for line_number, line in enumerate(content.splitlines(), start=1):
            for pattern in self.patterns:
                for match in pattern.finditer(line):
                    secret_value = match.group(1) if match.lastindex else match.group(0)
                    findings.append(
                        Finding(
                            file_path=file_path,
                            line_number=line_number,
                            detector=self.name,
                            provider=self.provider_name(),
                            secret=secret_value,
                            line_preview=line.strip(),
                        )
                    )
        return findings

    def has_keyword_context(self, line: str) -> bool:
        """Return True if the line contains contextual keywords that reinforce the match."""
        lowered = line.lower()
        return any(keyword in lowered for keyword in self.keywords)


def mask_secret(secret: str, visible: int = 4) -> str:
    """Return a masked representation of the secret for safe display."""
    if len(secret) <= visible * 2:
        return secret
    return f"{secret[:visible]}...{secret[-visible:]}"
