# SpecToTest

AI-powered Swagger/OpenAPI parser for automated test generation.

## Features

- Parse Swagger/OpenAPI endpoints
- Extract:
  - path
  - HTTP method
  - summary
  - operationId
  - tags
- Built-in validation for supported HTTP methods
- Pytest-based test architecture
- Mocked Swagger testing support

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
│   ├── conftest.py
│   ├── mock_data/
│   ├── happy_test_case/
│   ├── negative_test_case/
│   └── edge_case/
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
Phase 1 completed:
- Swagger JSON parsing
- Path extraction
- HTTP method validation
- Basic parser testing
- Mock testing with pytest