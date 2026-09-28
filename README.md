# SpecToTest

A Python-based Swagger 2.0 processing tool that parses API specifications,
extracts and resolves request/response schemas, and prepares structured metadata
for AI-assisted API test planning.

**Current scope: Swagger 2.0**

OpenAPI 3 support may be added in later phases.

## Why SpecToTest?

SpecToTest is a portfolio project focused on building a maintainable and
extensible API testing framework from scratch.

The project is developed incrementally, with automated testing, code quality
checks, and continuous integration throughout development.

## Project Goal

SpecToTest parses Swagger 2.0 specifications, extracts endpoint information,
resolves request and response schemas, and transforms them into structured
metadata.

The current phase introduces LLM integration for AI-assisted API test planning.

---

## Features

### Swagger Parsing

* Load Swagger specifications from URL or local JSON
* Parse API paths and supported HTTP methods
* Extract endpoint metadata
* Handle malformed or incomplete Swagger structures

### Schema Extraction and Resolution

* Extract request and response schemas
* Resolve Swagger `$ref` references
* Resolve array and nested references
* Resolve Swagger `allOf` schema compositions
* Extract schema and property metadata
* Process schemas into structured metadata

### AI Integration

* OpenAI Python SDK integration
* Secure API key configuration with environment variables
* Prompt generation from endpoint and schema metadata
* LLM client for AI communication
* Mocked LLM responses for isolated testing

### Testing and Code Quality

* Pytest unit tests
* Mock and monkeypatch-based testing
* Test coverage with pytest-cov
* Black formatting
* Ruff linting
* GitHub Actions CI

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

## Installation

Clone the repository:

```bash
git clone https://github.com/ozgemeva/SpecToTest.git
cd SpecToTest
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## AI Configuration

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key
```

The `.env` file is excluded from version control.

> Never commit API keys or other secrets to the repository.

---

## Running Tests

Run all tests:

```bash
python -m pytest
```

Run tests with coverage:

```bash
python -m pytest --cov=app --cov-report=term-missing
```

---

## Roadmap

### ✅ Phase 1 — Swagger Parser Engine

Swagger loading, validation, endpoint parsing, and metadata extraction.

### ✅ Phase 2 — Schema Extraction and Resolution

Request/response schema extraction, `$ref` resolution, `allOf` handling,
nested references, and structured schema metadata.

### 🚧 Phase 3 — AI Test Planning

LLM integration for AI-assisted API test planning.

Completed so far:

* OpenAI integration foundation
* Prompt builder
* LLM client
* Mocked LLM response testing

Next:

* Complete LLM client tests
* Perform the first real LLM request
* Parse and validate structured LLM output

---

## Code Quality

The project uses Black, Ruff, Pytest, and GitHub Actions for automated
formatting, linting, testing, and continuous integration.

```bash
python -m black . --check
python -m ruff check .
python -m pytest
```