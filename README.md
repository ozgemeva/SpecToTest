# SpecToTest
AI-powered Swagger/OpenAPI parser for automated test generation.

Current scope: **Swagger 2.0**  
OpenAPI 3 support may be added in later phases.

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

## Technologies 
- Python
- Pytest
- pytest-mock
- pytest-cov
- Requests
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
├── requirements.txt
└── README.md
```
---

## Installation

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
Phase 1 Completed
- Swagger JSON parsing
- Endpoint path extraction
- HTTP method validation
- Metadata extraction
- Local file and URL-based Swagger loading
- Mocked parser testing with Pytest
- Edge case and negative scenario testing
- Test coverage added
Phase 2 In Progress
- Request schema extraction
- Response schema extraction
- Swagger 2.0 body parameter handling
- Preparing parsed endpoint data for future test generation

## Roadmap
- Phase 1: Swagger parser engine
- Phase 2: Request/response schema extraction
- Phase 3: Test scenario generation
- Phase 4: AI-assisted test case creation
- Phase 5: Playwright/API test generation
- Phase 6: Test execution and reporting

## Code Quality

This project uses **Black** and **Ruff** to maintain a consistent and high-quality codebase.

* **Black** automatically formats the code according to a standard style, making it easier to read and review.
* **Ruff** performs fast linting, detects potential issues (such as unused imports, unused variables, and style violations), and can automatically fix many of them.

### Commands
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
