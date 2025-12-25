from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Optional

from rich.console import Console

from antarit import config
from antarit.detectors import (
    AWSAccessKeyDetector,
    AzureDetector,
    BitbucketTokenDetector,
    CircleCITokenDetector,
    DockerDetector,
    ElasticsearchDetector,
    GeminiDetector,
    GoogleAIDetector,
    FirebaseDetector,
    GCPDetector,
    GenericEntropyDetector,
    GithubTokenDetector,
    GitLabTokenDetector,
    StripeKeyDetector,
    JenkinsTokenDetector,
    JWTDetector,
    KubernetesDetector,
    MailgunTokenDetector,
    MongoDBDetector,
    MySQLDetector,
    OAuthTokenDetector,
    OpenAIDetector,
    PayPalDetector,
    PostgresDetector,
    RazorpayDetector,
    RedisDetector,
    SendGridTokenDetector,
    SlackTokenDetector,
    SupabaseDetector,
    TerraformDetector,
    TravisCITokenDetector,
    TwilioTokenDetector,
    VaultTokenDetector,
)
from antarit.detectors.base import BaseDetector, Finding
from antarit.scoring import Confidence, score
from antarit.utils.files import iter_files
from antarit.validators import passes_basic_checks, shannon_entropy

console = Console()


class Analyzer:
    def __init__(self, detectors: Optional[Iterable[BaseDetector]] = None):
        self.detectors: List[BaseDetector] = list(detectors or self._default_detectors())

    def _default_detectors(self) -> Iterable[BaseDetector]:
        return [
            AWSAccessKeyDetector(),
            AzureDetector(),
            GCPDetector(),
            GithubTokenDetector(),
            GitLabTokenDetector(),
            BitbucketTokenDetector(),
            CircleCITokenDetector(),
            TravisCITokenDetector(),
            JenkinsTokenDetector(),
            StripeKeyDetector(),
            OpenAIDetector(),
            GoogleAIDetector(),
            GeminiDetector(),
            SlackTokenDetector(),
            TwilioTokenDetector(),
            SendGridTokenDetector(),
            MailgunTokenDetector(),
            PayPalDetector(),
            RazorpayDetector(),
            FirebaseDetector(),
            SupabaseDetector(),
            GenericEntropyDetector(),
            MongoDBDetector(),
            PostgresDetector(),
            MySQLDetector(),
            RedisDetector(),
            ElasticsearchDetector(),
            JWTDetector(),
            OAuthTokenDetector(),
            DockerDetector(),
            KubernetesDetector(),
            TerraformDetector(),
            VaultTokenDetector(),
        ]

    def scan_path(
        self,
        path: Path,
        provider_filter: str | None = None,
        min_confidence: Confidence = Confidence.LOW,
    ) -> list[Finding]:
        """Walk the given path and return qualifying findings."""
        findings: list[Finding] = []
        if path.is_file():
            targets = [path]
        else:
            targets = list(iter_files(path))

        active_detectors = self._filter_detectors(provider_filter)

        for file_path in targets:
            try:
                content = file_path.read_text(errors="ignore")
            except (OSError, UnicodeDecodeError):
                console.print(f"[yellow]Skipping unreadable file: {file_path}")
                continue

            for detector in active_detectors:
                raw_findings = detector.detect(file_path, content)
                for finding in raw_findings:
                    if not passes_basic_checks(finding.secret):
                        continue
                    finding.entropy = shannon_entropy(finding.secret)
                    keyword_hit = detector.has_keyword_context(finding.line_preview or "")
                    finding.confidence = score(
                        entropy=finding.entropy,
                        provider_match=True,
                        has_keyword_context=keyword_hit,
                    ).value
                    if self._meets_confidence(finding.confidence, min_confidence):
                        findings.append(finding)

        return findings

    def _filter_detectors(self, provider_filter: str | None) -> list[BaseDetector]:
        if not provider_filter:
            return self.detectors
        provider_filter = provider_filter.lower()
        return [detector for detector in self.detectors if detector.provider_name() == provider_filter]

    def _meets_confidence(self, candidate: str, minimum: Confidence) -> bool:
        ranking = {Confidence.LOW.value: 0, Confidence.MEDIUM.value: 1, Confidence.HIGH.value: 2}
        return ranking.get(candidate, 0) >= ranking[minimum.value]
