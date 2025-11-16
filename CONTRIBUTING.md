# Contributing

Thanks for helping build Ziltrix — Sentinel Cognitive Hybridiser.

## Quick Start
1. Create a virtual env (Python 3.11):
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -U pip
   pip install -r requirements.txt -r requirements-dev.txt  # if present
   ```
2. Pre-commit:
   ```bash
   pip install pre-commit && pre-commit install
   pre-commit run --all-files
   ```
3. Run tests:
   ```bash
   pytest -q
   ```

## Style & Quality
- Black (format), Ruff (lint), isort (imports), Mypy (types).
- Conventional Commits for PR titles (enforced in CI), e.g., `feat: add ternary field operator`.

## Branching
- Feature: `feat/<short-slug>`
- Fix: `fix/<short-slug>`
- Chore/CI/Docs: `chore/<short-slug>`, `ci/<short-slug>`, `docs/<short-slug>`

## Security
- Never commit secrets. Use GitHub Actions secrets and local `.env` (ignored).
- Report vulnerabilities per [SECURITY.md](./SECURITY.md).
