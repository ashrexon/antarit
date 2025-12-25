from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from antarit.detectors.base import Finding, mask_secret


def serialize_findings(findings: Iterable[Finding]) -> str:
    payload = []
    for finding in findings:
        payload.append(
            {
                "file": str(Path(finding.file_path)),
                "line": finding.line_number,
                "provider": finding.provider,
                "detector": finding.detector,
                "confidence": finding.confidence,
                "secret": mask_secret(finding.secret),
                "entropy": finding.entropy,
                "line_preview": finding.line_preview,
            }
        )
    return json.dumps({"findings": payload, "count": len(payload)}, indent=2)
