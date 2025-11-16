# Ziltrix — Sentinel Cognitive Hybridiser

[![CI](https://github.com/wizardaax/ziltrix-sch-core/actions/workflows/ci.yml/badge.svg)](https://github.com/wizardaax/ziltrix-sch-core/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

Ziltrix SCH (Sentinel Cognitive Hybridiser) is a core engine for symbolic-cognitive computation built around recursive field math: Lucas/Fibonacci sequences, golden-ratio (φ) structures, ternary logic/fields, entropy pumps, and glyph-based symbolic operators. The focus is on mathematically faithful primitives with high reliability and security.

Where Intelligence Becomes Intelligent.

## Features
- Recursive Lucas/Fibonacci operators and φ-aligned transforms
- Ternary field structures and composable symbolic glyph pipelines
- Deterministic entropy extraction and cryptographic hygiene hooks
- Strong CI gates (lint, types, tests, security)

## Quick Start
```bash
# Python 3.11 recommended
python -m venv .venv && source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt  # if present

# Quality (optional but recommended)
pip install pre-commit && pre-commit install
pre-commit run --all-files

# Tests
pytest -q
```

## Development
- Code style: Black, Ruff, isort; types via mypy (see pyproject.toml and mypy.ini).
- Commit style: Conventional Commits; PR titles enforced in CI.
- Folder layout: prefer `src/` for packages and `tests/` for tests.

## CI/CD
- GitHub Actions runs on pushes and PRs to main.
- Jobs auto-detect Python/Node projects and run only relevant steps.
- Security scanning via Bandit.

## Contributing
See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

## Security
See [SECURITY.md](./SECURITY.md). Report issues privately.

## License
MIT — see [LICENSE](./LICENSE).
