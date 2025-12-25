from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, Iterator

from antarit import config


def is_binary(path: Path, chunk_size: int = 1024) -> bool:
    """Heuristically determine if a file is binary by scanning the first chunk."""
    try:
        with path.open("rb") as file_handle:
            chunk = file_handle.read(chunk_size)
            if b"\0" in chunk:
                return True
            if not chunk:
                return False
            printable = bytearray(range(32, 127)) + b"\n\r\t\b"
            nontext = sum(byte not in printable for byte in chunk)
            return (nontext / len(chunk)) > 0.30
    except (OSError, UnicodeDecodeError):
        return True


def iter_files(
    root: Path,
    ignored_dirs: Iterable[str] = config.DEFAULT_IGNORED_DIRS,
    ignored_extensions: Iterable[str] = config.DEFAULT_IGNORED_EXTENSIONS,
) -> Iterator[Path]:
    """Yield file paths under root, skipping ignored directories and binary files."""
    for current_root, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for filename in files:
            path = Path(current_root) / filename
            if path.suffix.lower() in ignored_extensions:
                continue
            if is_binary(path):
                continue
            yield path
