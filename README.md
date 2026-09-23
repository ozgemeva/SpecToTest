# SpecToTest

A Python-based Swagger 2.0 processing tool that parses API specifications, extracts and resolves request/response schemas, and prepares structured metadata for automated API test generation.

**Current scope: Swagger 2.0**

OpenAPI 3 support may be added in later phases.

## Why SpecToTest?

SpecToTest is a portfolio project focused on building a maintainable and extensible API testing framework from scratch.

The project is developed incrementally, with each phase introducing a new capability while maintaining automated testing, code quality checks, and continuous integration.

## Project Goal

SpecToTest is designed to parse Swagger 2.0 specifications, extract endpoint information, resolve request and response schemas, and transform schema definitions into structured metadata.

The long-term goal is to use this information to generate API test scenarios and eventually convert them into executable API and Playwright tests.

---

## Features

### Swagger Parsing

* Load Swagger 2.0 specifications from a remote URL
* Fall back to a local Swagger JSON file
* Parse API paths and supported HTTP methods
* Extract endpoint metadata such as summary, operation ID, tags, consumes, and produces
* Handle malformed or incomplete Swagger structures

### Schema Extraction and Resolution

* Extract request body and HTTP 200 response schemas
* Resolve Swagger `$ref` references to model definitions
* Resolve references inside array items
* Extract schema-level metadata such as type, required fields, properties, and XML metadata
* Extract property-level metadata including type, format, enum, example, items, `$ref`, and required status
* Resolve nested schema references
* Process resolved schemas into structured metadata through `SchemaProcessor`

### Testing and Code Quality

* Pytest-based unit testing
* Mocked Swagger data for isolated tests
* Test coverage reporting with pytest-cov
* Code formatting with Black
* Static analysis with Ruff
* Continuous integration with GitHub Actions

GitHub Actions automatically installs dependencies, checks Black formatting, runs Ruff linting, and executes the complete Pytest test suite.

---

## Technologies

* Python 3.11+
* Requests
* Pytest
* pytest-mock
* pytest-cov
* Black
* Ruff
* GitHub Actions

---

## Project Structure

```text
SpecToTest/
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── api_parser/
│   │   └── swagger_parser.py
│   │
│   ├── schema/
│   │   ├── schema_extractor.py
│   │   ├── schema_processor.py
│   │   └── schema_resolver.py
│   │
│   └── config.py
│
├── docs/
│
├── spec/
│
├── tests/
│   ├── unit_tests/
│   │   ├── mock_data/
│   │   ├── phase_1_swagger_data/
│   │   └── phase_2_schema_extraction/
│   │
│   └── conftest.py
│
├── main.py
├── pyproject.toml
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ozgemeva/SpecToTest.git
cd SpecToTest
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

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

Run tests with verbose output:

```bash
python -m pytest -v
```

Run tests with coverage:

```bash
python -m pytest --cov=app --cov-report=term-missing
```

---

## Test Strategy

The test suite covers:

* **Happy paths** — valid Swagger structures and expected behavior
* **Negative cases** — invalid inputs, missing data, and malformed structures
* **Edge cases** — empty paths, unknown fields, missing response data, and schema reference variations

Phase 2 schema-processing components are fully covered by unit tests.

---

## Roadmap

### ✅ Phase 1 — Swagger Parser Engine

Swagger loading, validation, endpoint parsing, HTTP method handling, and endpoint metadata extraction.

### ✅ Phase 2 — Schema Extraction and Resolution

Request/response schema extraction, `$ref` resolution, array references, schema and property metadata extraction, nested reference resolution, and schema processing.

### 🚧 Phase 3 — Test Scenario Generation

Generate positive, negative, and edge-case test scenarios from extracted schema information.

### 🔜 Phase 4 — AI-Assisted Test Case Creation

Improve generated scenarios with AI, generate readable test descriptions, and suggest additional edge cases.

### 🔜 Phase 5 — Playwright and API Test Generation

Generate executable API tests with reusable fixtures and assertions.

### 🔜 Phase 6 — Test Execution and Reporting

Execute generated tests and produce execution and coverage reports.

---

## Code Quality

SpecToTest uses automated quality checks throughout development:

* **Black** for consistent code formatting
* **Ruff** for linting and static analysis
* **Pytest** for automated unit testing
* **pytest-cov** for coverage reporting
* **GitHub Actions** for continuous integration

Before pushing changes, the project can be validated locally with:

```bash
python -m black .
python -m black . --check
python -m ruff check .
python -m pytest -v
```