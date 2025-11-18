# GitHub Copilot Instructions for Ziltrix SCH Core

This repository contains the Ziltrix SCH (Sentinel Cognitive Hybridiser) core engine for symbolic-cognitive computation. Follow these instructions to maintain code quality and consistency.

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
