from __future__ import annotations

import math
from typing import Iterable

from antarit import config


def shannon_entropy(value: str) -> float:
    """Calculate Shannon entropy for a string."""
    if not value:
        return 0.0
    frequencies = {char: value.count(char) for char in set(value)}
    entropy = 0.0
    length = len(value)
    for count in frequencies.values():
        p_x = count / length
        entropy -= p_x * math.log2(p_x)
    return entropy


def passes_basic_checks(
    value: str,
    min_length: int = config.MIN_SECRET_LENGTH,
    entropy_threshold: float = config.ENTROPY_THRESHOLD,
    required_charsets: Iterable[str] | None = None,
) -> bool:
    """Validate that the value is long and complex enough to be a candidate secret."""
    if len(value) < min_length:
        return False

    entropy = shannon_entropy(value)
    if entropy < entropy_threshold:
        return False

    if required_charsets:
        for charset in required_charsets:
            if not any(char in charset for char in value):
                return False

    return True
