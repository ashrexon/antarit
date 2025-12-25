from __future__ import annotations

from enum import Enum


class Confidence(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


def score(entropy: float | None, provider_match: bool, has_keyword_context: bool) -> Confidence:
    """Calculate a coarse confidence rating for a finding."""
    entropy = entropy or 0.0

    if provider_match and entropy >= 4.5:
        return Confidence.HIGH
    if entropy >= 4.2 and has_keyword_context:
        return Confidence.HIGH
    if entropy >= 4.0 and provider_match:
        return Confidence.MEDIUM
    if entropy >= 3.5:
        return Confidence.MEDIUM
    return Confidence.LOW
