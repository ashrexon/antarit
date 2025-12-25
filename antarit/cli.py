from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Optional

import click

from antarit import __version__, config
from antarit.analyzer import Analyzer
from antarit.output.console import print_findings
from antarit.output.json import serialize_findings
from antarit.scoring import Confidence


def clone_repo(repo_url: str) -> Path:
    """Clone a git repository into a temporary directory for scanning."""
    destination = Path(tempfile.mkdtemp(prefix="antarit-"))
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, str(destination)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        shutil.rmtree(destination, ignore_errors=True)
        raise click.ClickException(f"Failed to clone repository: {exc}")
    return destination


@click.group()
@click.version_option(version=__version__)
def main() -> None:
    """Antarit: Scan for exposed SaaS secrets in code and config."""


@main.command()
@click.argument("path", required=False, type=click.Path(path_type=Path))
@click.option("--repo", "repo_url", type=str, help="Git repository URL to clone and scan.")
@click.option("--json", "json_output", is_flag=True, help="Emit machine-readable JSON output.")
@click.option(
    "--confidence",
    type=click.Choice([c.value.lower() for c in Confidence], case_sensitive=False),
    default="low",
    show_default=True,
    help="Minimum confidence level to report.",
)
@click.option(
    "--provider",
    "provider_filter",
    type=click.Choice(config.PROVIDERS, case_sensitive=False),
    help="Only run detectors for a specific provider.",
)
def scan(path: Optional[Path], repo_url: Optional[str], json_output: bool, confidence: str, provider_filter: str | None) -> None:
    """Scan a path or git repository for secrets."""
    temp_repo_path: Path | None = None
    try:
        if repo_url:
            temp_repo_path = clone_repo(repo_url)
            target_path = temp_repo_path
        else:
            target_path = path or Path(".")

        if not target_path.exists():
            raise click.ClickException(f"Path not found: {target_path}")

        analyzer = Analyzer()
        min_confidence = Confidence(confidence.upper())
        findings = analyzer.scan_path(
            target_path,
            provider_filter=provider_filter,
            min_confidence=min_confidence,
        )

        if json_output:
            click.echo(serialize_findings(findings))
        else:
            print_findings(findings)
    finally:
        if temp_repo_path and temp_repo_path.exists():
            shutil.rmtree(temp_repo_path, ignore_errors=True)
