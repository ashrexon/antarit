# Antarit

Antarit is a CLI-based security scanner focused on detecting exposed SaaS API keys, tokens, and secrets in source code, configuration, and git repositories. It favors a clean, modular architecture to make adding new providers, outputs, and validation strategies straightforward.

## Features
- Provider-specific detectors for cloud (AWS, GCP, Azure), CI/CD (GitHub, GitLab, Bitbucket, CircleCI, Travis CI, Jenkins), SaaS (Slack, Twilio, SendGrid, Mailgun, Stripe, PayPal, Razorpay, Firebase, Supabase), AI APIs (OpenAI, Google AI, Gemini), and data stores (PostgreSQL, MongoDB, MySQL, Redis, Elasticsearch).
- Entropy and length validation to reduce false positives.
- Confidence scoring (LOW, MEDIUM, HIGH) combining entropy and context.
- Rich console output or JSON for automation.
- Git repository scanning via `--repo` without mixing CLI and scanning logic.

## Installation
```bash
pip install -e .
```

## Usage
- Scan a local path:
```bash
antarit scan .
```
- Scan a git repository:
```bash
antarit scan --repo https://github.com/example/project.git
```
- JSON output and confidence filtering:
```bash
antarit scan . --json --confidence high
```
- Provider filtering:
```bash
antarit scan . --provider aws
```

## Development
- Requires Python 3.10+.
- Entry point: `python -m antarit --help`.
- Extend by adding detectors under `antarit/detectors` and wiring them into the analyzer.
