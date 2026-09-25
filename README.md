# SpecToTest

A Python-based Swagger 2.0 processing tool that parses API specifications,
extracts and resolves request/response schemas, and prepares structured
metadata for AI-assisted API test planning.

**Current scope: Swagger 2.0**

OpenAPI 3 support may be added in later phases.

## Why SpecToTest?

SpecToTest is a portfolio project focused on building a maintainable and
extensible API testing framework from scratch.

The project is developed incrementally, with each phase introducing a new
capability while maintaining automated testing, code quality checks, and
continuous integration.

## Project Goal

SpecToTest is designed to parse Swagger 2.0 specifications, extract endpoint
information, resolve request and response schemas, and transform schema
definitions into structured metadata.

The current development phase introduces LLM integration so that the structured
API information produced by the parser and schema-processing components can be
used for AI-assisted API test planning.

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

### AI Integration

* OpenAI Python SDK integration
* Secure API key configuration using environment variables
* `.env` support with `python-dotenv`
* AI client foundation for LLM communication

### Testing and Code Quality

* Pytest-based unit testing
* Mocked Swagger data for isolated tests
* Test coverage reporting with pytest-cov
* Code formatting with Black
* Static analysis with Ruff
* Continuous integration with GitHub Actions

GitHub Actions automatically installs dependencies, checks Black formatting,
runs Ruff linting, and executes the complete Pytest test suite.

---

## Technologies

* Python 3.11+
* Requests
* OpenAI Python SDK
* python-dotenv
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
│   ├── ai/
│   │   ├── __init__.py
│   │   └── ai_client.py
│   │
│   └── config.py
│
├── docs/
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

## AI Configuration

SpecToTest uses the OpenAI API for AI-assisted API test planning.

API credentials are kept outside the source code using environment variables.

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key
```

The `.env` file is excluded from version control through `.gitignore`.

Environment variables are loaded using `python-dotenv`:

```python
from dotenv import load_dotenv

load_dotenv()
```

The API key can then be accessed through the environment:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

> Never commit API keys or other secrets to the repository.

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

Phase 2 schema-processing components are covered by unit tests.

---

## Roadmap

### ✅ Phase 1 — Swagger Parser Engine

Swagger loading, validation, endpoint parsing, HTTP method handling, and
endpoint metadata extraction.

### ✅ Phase 2 — Schema Extraction and Resolution

Request/response schema extraction, `$ref` resolution, array references,
schema and property metadata extraction, nested reference resolution, and
schema processing.

### 🚧 Phase 3 — AI Test Planning

Integrate an LLM into SpecToTest and use the structured endpoint and schema
information produced by Phase 1 and Phase 2 to support AI-assisted API test
planning.

Current work:

* AI integration foundation
* OpenAI Python SDK integration
* Secure API key configuration
* Environment variable loading
* AI client setup

---

## Documentation

* OpenAI API Documentation: https://developers.openai.com/api/docs
* OpenAI Python SDK: https://github.com/openai/openai-python
* python-dotenv: https://pypi.org/project/python-dotenv/
* Python `os.getenv`: https://docs.python.org/3/library/os.html#os.getenv

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