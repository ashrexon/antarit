from __future__ import annotations

from pathlib import Path
from typing import Final, Iterable

# Default directories to ignore during scanning to avoid noisy or irrelevant paths.
DEFAULT_IGNORED_DIRS: Final[set[str]] = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "node_modules",
    "__pycache__",
}

# File extensions that are commonly binary or not helpful for scanning.
DEFAULT_IGNORED_EXTENSIONS: Final[set[str]] = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".ico",
    ".exe",
    ".dll",
    ".so",
    ".dylib",
    ".pdf",
    ".zip",
    ".gz",
    ".tar",
    ".7z",
}

# Sensible defaults for entropy-based validation.
MIN_SECRET_LENGTH: Final[int] = 20
ENTROPY_THRESHOLD: Final[float] = 4.0

# Provider choices exposed through the CLI. Extend this list as new providers are added.
PROVIDERS: Final[tuple[str, ...]] = (
    "aws",
    "gcp",
    "azure",
    "github",
    "gitlab",
    "bitbucket",
    "circleci",
    "travisci",
    "jenkins",
    "slack",
    "twilio",
    "sendgrid",
    "mailgun",
    "stripe",
    "openai",
    "googleai",
    "gemini",
    "paypal",
    "razorpay",
    "firebase",
    "supabase",
    "mongodb",
    "postgresql",
    "mysql",
    "redis",
    "elasticsearch",
    "jwt",
    "oauth",
    "docker",
    "kubernetes",
    "terraform",
    "vault",
    "generic",
)


def should_ignore_dir(path: Path, ignored_dirs: Iterable[str] = DEFAULT_IGNORED_DIRS) -> bool:
    """Return True if the given directory name should be skipped."""
    return path.name in ignored_dirs


def should_ignore_file(path: Path, ignored_extensions: Iterable[str] = DEFAULT_IGNORED_EXTENSIONS) -> bool:
    """Return True if the file extension indicates we should skip scanning."""
    return path.suffix.lower() in ignored_extensions
