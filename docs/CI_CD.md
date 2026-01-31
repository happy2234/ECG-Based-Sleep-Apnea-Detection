# Continuous Integration & Testing

This document outlines the automated testing and CI/CD setup for the ECG-Based Sleep Apnea Detection project.

## GitHub Actions Workflows

### 1. Python Tests & Code Quality (tests.yml)

Automated testing runs on every push and pull request to `main` and `develop` branches.

**Workflow Components:**

- **Python Testing**
  - Tests on Python 3.11, 3.12, and 3.13
  - Unit tests with pytest
  - Coverage reporting to Codecov
  - Parallel test execution with pytest-xdist

- **Code Quality Checks**
  - Black formatting validation
  - isort import sorting
  - Pylint code analysis
  - Maximum line length: 127 characters

- **Security Analysis**
  - Bandit for security vulnerabilities
  - Safety for dependency vulnerabilities
  - JSON report generation

- **Build Status**
  - Final build status check
  - Deployment readiness verification

### 2. Test Coverage

**Current Coverage:**
- Unit tests: Core modules
- Integration tests: Feature pipeline
- API tests: Endpoint validation

**Target Coverage:** >80% by Week 10

### 3. Status Badges

Add these badges to your README:

```markdown
![Tests](https://github.com/happy2234/ECG-Based-Sleep-Apnea-Detection/workflows/Python%20Tests%20%26%20Code%20Quality/badge.svg)
![Python Version](https://img.shields.io/badge/Python-3.13-blue)
![Code Coverage](https://img.shields.io/codecov/c/github/happy2234/ECG-Based-Sleep-Apnea-Detection)
```

### 4. Running Tests Locally

Before pushing, run tests locally:

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_data.py -v

# Run tests in parallel
pytest tests/ -n auto
```

### 5. Code Quality Checks

```bash
# Format code with Black
black src/ tests/

# Sort imports with isort
isort src/ tests/

# Check with Pylint
pylint src/

# Security check with Bandit
bandit -r src/
```

### 6. Workflow Triggers

| Event | Trigger | Action |
|-------|---------|--------|
| Push to main | All commits | Run full test suite |
| Push to develop | All commits | Run full test suite |
| Pull Request | To main/develop | Run tests before merge |
| Schedule | Daily 00:00 UTC | Dependency security scan |

### 7. Test Results

- View test results in GitHub Actions tab
- Download artifacts (coverage reports)
- Codecov integration for coverage tracking

### 8. CI/CD Pipeline

```
Code Push
    │
    ├─► Python Linting
    │    └─► PASS/FAIL
    │
    ├─► Unit Tests (Python 3.11, 3.12, 3.13)
    │    ├─► Code Coverage
    │    └─► PASS/FAIL
    │
    ├─► Code Quality Analysis
    │    ├─► Black Formatting
    │    ├─► isort Import Sorting
    │    ├─► Pylint Analysis
    │    └─► PASS/FAIL
    │
    ├─► Security Scanning
    │    ├─► Bandit Security Check
    │    ├─► Dependency Vulnerabilities
    │    └─► PASS/FAIL
    │
    └─► Build Status
         └─► Ready for Deployment/Merge
```

### 9. Troubleshooting

**Common Issues:**

1. **Tests fail locally but pass in CI**
   - Check Python version: `python --version`
   - Ensure all dependencies installed: `pip install -r requirements.txt`

2. **Coverage is lower than expected**
   - Run with detailed report: `pytest --cov-report=html`
   - Check uncovered lines in htmlcov/index.html

3. **Import errors in tests**
   - Verify __init__.py files exist
   - Check sys.path includes src/ directory

4. **Code formatting issues**
   - Run Black: `black src/ tests/`
   - Check line length: `flake8 src/ --max-line-length=127`

### 10. Extending CI/CD

**Future additions (Week 10):**
- Docker build testing
- Performance benchmarking
- Deployment testing
- Automated release management

---

**Status**: Active  
**Last Updated**: February 1, 2026
