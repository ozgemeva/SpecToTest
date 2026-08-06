# SpecToTest
AI-powered Swagger/OpenAPI parser for automated test generation.
Current scope: **Swagger 2.0**  
OpenAPI 3 support may be added in later phases.

## Why SpecToTest?
SpecToTest is a portfolio project focused on building a maintainable and extensible API testing framework from scratch. Each development phase adds a new capability while keeping the project fully tested and production-quality.

## Project Goal
SpecToTest is a QA automation tool designed to read Swagger/OpenAPI specifications and prepare structured endpoint data for future automated test generation.
The long-term goal is to generate API test scenarios and later convert them into executable Playwright/API tests.

---

## Features
- Parse Swagger 2.0 JSON specifications
- Extract endpoint metadata:
  - path
  - HTTP method
  - summary
  - operation_id
  - tags
  - consumes
  - produces
- Validate supported HTTP methods
- Skip invalid or malformed endpoint definitions safely
- Support mocked Swagger data for unit testing
- Pytest-based test architecture
- Test coverage reporting with pytest-cov
- Extract request content types
- Extract response content types
- Extract HTTP 200 response schemas
- Code formatting with Black
- Static analysis with Ruff
- Continuous integration with GitHub Actions
    -This project uses **GitHub Actions** to automatically:
    - Install project dependencies
    - Check code formatting with Black
    - Run Ruff linting
    - Execute the complete Pytest test suite
    
## Technologies
- Python 3.11+
- Requests
- Pytest
- pytest-mock
- pytest-cov
- Black
- Ruff
---

## Project Structure

```text
SpecToTest/
├── app/
│   ├── api_parser/
│   │   └── swagger_parser.py
│   └── config.py
│
├── tests/
|   ├── unit_tests/  
│   ├── conftest.py
│
├── pyproject.toml
├── requirements.txt
└── README.md
```
---

## Installation

```bash
git clone https://github.com/ozgemeva/SpecToTest.git
cd SpecToTest
```

Create virtual environment:

```bash
python -m venv venv
```

Activate venv:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```
---

## Running Tests

Run all tests:

```bash
python -m pytest
```

Run all tests with verbose output:

```bash
python -m pytest -v
```
Run all tests and show print outputs:

```bash
python -m pytest -v -s
```
## Run Tests with Coverage

```bash
pytest -s --cov=app --cov-report=term-missing
pytest -v --cov=app 
```
---
## Test Categories

### Happy Path Tests
Tests valid Swagger/OpenAPI inputs and expected parser behavior.

### Negative Tests
Tests invalid inputs and verifies invalid endpoints are skipped safely.

### Edge Case Tests
Tests unusual or boundary scenarios such as:
- missing summary
- missing tags
- empty paths
- malformed endpoint details
---

## Current Status

### Phase 1 Completed
- Swagger JSON parsing
- Endpoint extraction
- Metadata extraction
- URL and local Swagger loading
- Validation
- Unit tests
- Coverage reporting

### Phase 2 Completed
- Request content type extraction
- Response content type extraction
- HTTP 200 response schema extraction
- Swagger body parameter handling
- Black formatting
- Ruff linting

## Roadmap
### Phase 1 — Swagger Parser Engine

* Load Swagger 2.0 specifications from a remote URL
* Fall back to a local JSON file
* Extract paths, HTTP methods, summaries, tags, and operation IDs
* Validate malformed Swagger structures

### Phase 2 — Request and Response Schema Extraction

* Extract request content types
* Extract response content types
* Extract HTTP 200 response schemas
* Add unit tests for happy, negative, and edge cases
* Add Black and Ruff code-quality checks

### Phase 3 — Test Scenario Generation

* Generate positive, negative, and edge-case scenarios
* Map schemas to test inputs
* Define expected status codes and assertions

#### Phase 4 — AI-Assisted Test Case Creation

* Use AI to improve generated test scenarios
* Generate readable test descriptions
* Suggest additional edge cases

#### Phase 5 — Playwright and API Test Generation

* Generate executable API tests
* Generate Playwright-based test files
* Create reusable fixtures and assertions

#### Phase 6 — Test Execution and Reporting

* Execute generated tests
* Collect execution results
* Produce test reports and coverage summaries


## Code Quality

This project uses **Black** and **Ruff** to maintain a consistent and high-quality codebase.

* **Black** automatically formats the code according to a standard style, making it easier to read and review.

* **Ruff** performs fast linting, detects potential issues (such as unused imports, unused variables, and style violations), and can automatically fix many of them.

### Command
Format the project:

```bash
python -m black .
```

Check formatting:

```bash
python -m black . --check
```

Run linting:

```bash
python -m ruff check .
```

Automatically fix linting issues:

```bash
python -m ruff check . --fix
```
