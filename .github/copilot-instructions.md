# GitHub Copilot Instructions for Ziltrix SCH Core

This repository contains the Ziltrix SCH (Sentinel Cognitive Hybridiser) core engine for symbolic-cognitive computation. Follow these instructions to maintain code quality and consistency.

## CRITICAL: Agent Operational Rules

### 1. GENERAL RULES
- Do NOT modify the entire repository without explicit user instruction.
- Do NOT run cleanup operations on the whole repo.
- Do NOT attempt to remove or "clean duplicates" unless explicitly requested.
- Do NOT delete or modify binary files (PDF, PNG, JPG, ZIP, EXE).
- Do NOT generate or modify CI workflows automatically.
- Do NOT start repeated task loops or retry jobs.

### 2. FILE & DIRECTORY RULES
- All PDF files must remain stored in `/docs/pdfs/` unless the user instructs otherwise.
- Never move, rename, or delete any PDF without explicit user confirmation.
- Never create extra folders for PDFs.
- Never scan or diff PDFs unless requested.

### 3. PULL REQUEST POLICY
- PRs must contain real, meaningful changes.
- If no changes are required, do NOT create a PR.
- Do NOT claim the repository is "clean" unless files were actually modified.
- Do NOT reopen closed PRs.
- Do NOT run the same task multiple times.

### 4. ALLOWED ACTIONS
- Format Python files with ruff/black when instructed.
- Run pytest only when explicitly asked.
- Fix or modify a single file or specific directory when asked.
- Suggest improvements without executing them automatically.
- Create PRs ONLY for tasks explicitly requested by the user.
- Only operate on one task at a time.

### 5. FORBIDDEN ACTIONS
- Do NOT run repo-wide cleanups.
- Do NOT delete or modify files autonomously.
- Do NOT re-run tasks automatically after finishing.
- Do NOT modify `.github/workflows/` unless explicitly requested.
- Do NOT open more than one PR per task.
- Do NOT trigger MCP server loops.

### 6. TASK EXECUTION POLICY
1. Validate user instruction.
2. Ensure the task is scoped to a specific file or directory.
3. Ask for confirmation if the scope is unclear.
4. Apply changes ONLY to the requested path.
5. Generate one clean PR containing only those changes.
6. Stop immediately after completing the task.
7. Do NOT retry.

### 7. FORCE STOP CONDITION
If a task results in:
- no diffs  
- no modified files  
- empty PR  

Then:
- exit immediately  
- do NOT create a PR  
- do NOT say "clean"  
- do NOT re-run  

### 8. SAFETY GUARD
If more than one Copilot-created PR exists:
- halt all running tasks
- close the newest PR
- notify the user for manual review

## General Guidelines

### Python Version and Style
- **Python Version**: Use Python 3.10 or newer (3.11 recommended)
- **Code Style**: Follow PEP 8 with modifications defined in `pyproject.toml` and `ruff.toml`
- **Line Length**: 100 characters maximum
- **Type Hints**: Always use type hints for function parameters and return values (`disallow_untyped_defs = True` in mypy.ini)
- **Imports**: Use isort for import organization (black profile)

### Code Quality Tools
All code must pass the following checks:
- **Ruff**: Linting and formatting (`ruff check .` and `ruff format --check .`)
- **Black**: Code formatting (`black --check .`)
- **Mypy**: Static type checking (`mypy .`)
- **Pytest**: All tests must pass (`pytest -q`)

### Security
- **Never commit secrets** or credentials. Use GitHub Actions secrets and local `.env` files (which are gitignored)
- Security scanning via **Bandit** runs in CI
- Report vulnerabilities per [SECURITY.md](../SECURITY.md)

## Project Structure

```
.
├── tests/           # Test files (test_*.py or *_test.py)
├── src/             # Future package code (currently not present)
├── pyproject.toml   # Python project configuration
├── mypy.ini         # Mypy configuration
├── ruff.toml        # Ruff configuration
├── pytest.ini       # Pytest configuration
└── .github/         # GitHub configuration and workflows
```

## Development Workflow

### Setting Up Development Environment
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -U pip
pip install -U ruff black mypy pytest pytest-cov

# Install pre-commit hooks (optional but recommended)
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

### Running Tests
```bash
# Run all tests
pytest -q

# Run with coverage
pytest -q --cov --cov-report=xml

# Run specific test
pytest tests/test_smoke.py -v
```

### Linting and Formatting
```bash
# Check with Ruff
ruff check .

# Auto-fix with Ruff
ruff check --fix .

# Format check with Ruff
ruff format --check .

# Format with Ruff
ruff format .

# Check with Black
black --check .

# Format with Black
black .

# Type check with Mypy
mypy .
```

## Commit and PR Guidelines

### Commit Messages
- Use **Conventional Commits** format (enforced in CI)
- Examples:
  - `feat: add ternary field operator`
  - `fix: correct Lucas sequence calculation`
  - `docs: update README with new features`
  - `test: add tests for entropy extraction`
  - `chore: update dependencies`
  - `ci: improve GitHub Actions workflow`

### Branch Naming
- Feature: `feat/<short-slug>`
- Fix: `fix/<short-slug>`
- Chore/CI/Docs: `chore/<short-slug>`, `ci/<short-slug>`, `docs/<short-slug>`

### Pull Requests
- PR titles must follow Conventional Commits format
- Ensure all CI checks pass before merging
- Reference related issues in PR description

## Domain-Specific Context

Ziltrix SCH focuses on:
- **Recursive Lucas/Fibonacci operators** and φ-aligned transforms
- **Ternary field structures** and composable symbolic glyph pipelines
- **Deterministic entropy extraction** and cryptographic hygiene hooks
- **Mathematical faithfulness** with high reliability and security

When writing code:
- Prioritize mathematical accuracy and precision
- Ensure cryptographic operations follow best practices
- Document complex mathematical operations thoroughly
- Write tests that verify mathematical properties

## CI/CD

GitHub Actions workflows run automatically on:
- Push to main branch
- Pull requests to main branch
- Changes to Python files, pyproject.toml, or requirements files

CI includes:
- Multi-version Python testing (3.10, 3.11, 3.12, 3.13)
- Ruff linting and formatting checks
- Black formatting checks
- Mypy type checking
- Pytest with coverage reporting
- Security scanning with Bandit (via CodeQL)
- Semantic PR title validation

## Common Tasks

### Adding a New Feature
1. Create a feature branch: `git checkout -b feat/my-feature`
2. Write tests first (TDD approach preferred)
3. Implement the feature
4. Run linting and tests locally
5. Commit with conventional commit message
6. Push and create PR

### Fixing a Bug
1. Create a fix branch: `git checkout -b fix/bug-description`
2. Write a failing test that reproduces the bug
3. Fix the bug
4. Ensure test passes and all checks pass
5. Commit and create PR

### Adding Tests
- Test files must be in `tests/` directory
- Name test files: `test_*.py` or `*_test.py`
- Use descriptive test function names: `test_<what_is_being_tested>`
- Use type hints in test functions
- Keep tests focused and atomic

## Code Style Examples

### Function Definition
```python
def calculate_fibonacci_ratio(n: int) -> float:
    """Calculate the ratio of consecutive Fibonacci numbers.
    
    Args:
        n: The index of the Fibonacci number (must be >= 2)
        
    Returns:
        The ratio F(n)/F(n-1), which approaches φ (golden ratio)
        
    Raises:
        ValueError: If n < 2
    """
    if n < 2:
        raise ValueError("n must be at least 2")
    # Implementation here
    return result
```

### Type Hints
```python
from typing import List, Dict, Optional, Tuple

def process_glyphs(
    glyphs: List[str], 
    config: Dict[str, int],
    max_depth: Optional[int] = None
) -> Tuple[bool, str]:
    """Process symbolic glyphs with given configuration."""
    # Implementation
    return success, message
```

### Test Example
```python
def test_fibonacci_ratio_convergence() -> None:
    """Test that Fibonacci ratio converges to golden ratio."""
    ratio = calculate_fibonacci_ratio(100)
    golden_ratio = (1 + 5 ** 0.5) / 2
    assert abs(ratio - golden_ratio) < 1e-10
```

## Additional Notes

- When in doubt, refer to existing code patterns in the repository
- Prefer clarity over cleverness
- Document non-obvious mathematical operations
- Use meaningful variable names that reflect mathematical concepts
- Keep functions focused and small (single responsibility principle)
