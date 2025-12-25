from __future__ import annotations

from pathlib import Path
from typing import Iterable

from rich.console import Console
from rich.table import Table
from rich.text import Text

from antarit.detectors.base import Finding, mask_secret
from antarit.scoring import Confidence

console = Console()


def _print_header() -> None:
    console.print("                             [bold cyan]Antarit - Secret Exposure Mapper v1.0[/bold cyan]")
    console.print("                              Developed by Yash Shendge - Ashrexon")
    console.print("                               https://github.com/ashrexon\n")


def _confidence_style(confidence: Confidence) -> str:
    if confidence is Confidence.HIGH:
        return "bold red"
    if confidence is Confidence.MEDIUM:
        return "yellow"
    return "cyan"


def print_findings(findings: Iterable[Finding]) -> None:
    _print_header()
    findings_list = list(findings)
    if not findings_list:
        console.print(":white_check_mark: No secrets found.")
        return

    table = Table(title="Antarit Findings", show_lines=True)
    table.add_column("File", overflow="fold")
    table.add_column("Line", justify="right")
    table.add_column("Provider")
    table.add_column("Detector")
    table.add_column("Confidence")
    table.add_column("Secret (masked)")

    for finding in findings_list:
        confidence = Confidence(finding.confidence or Confidence.LOW)
        table.add_row(
            str(Path(finding.file_path)),
            str(finding.line_number),
            finding.provider,
            finding.detector,
            Text(confidence.value, style=_confidence_style(confidence)),
            mask_secret(finding.secret),
        )

    console.print(table)
    console.print(f":mag_right: Findings: {len(findings_list)}")
