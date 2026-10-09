from types import SimpleNamespace

import pytest

from app.ai.llm_client import LlmClient
from tests.unit_tests.mock_data.llm_md.llm_request_md import (
    LLM_REQUEST,
)
from tests.unit_tests.mock_data.llm_md.llm_response_md import (
    INVALID_LLM_RESPONSE,
    LLM_RESPONSE,
    LLM_RESPONSE_LIST,
    LLM_RESPONSE_MISSING_FIELD,
    LLM_RESPONSE_WITH_NODICT_NOLIST,
    TEMP_PROMPT,
)


# cteate fake client for OpenAI
def create_mock_llm_client(monkeypatch, mock_data):
    llm_client = LlmClient()

    # create fake responses.output
    def fake_create(**kwargs):
        return SimpleNamespace(output_text=mock_data)

    # during test, we use fake_create method instead of "self.client.responses.create()"
    monkeypatch.setattr(
        llm_client.client.responses,
        "create",
        fake_create,
    )
    return llm_client


@pytest.fixture
def llm_client_with_mock(monkeypatch, llm_client_with_llm_response):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-test-key")
    return create_mock_llm_client(monkeypatch, llm_client_with_llm_response)


@pytest.fixture
def llm_client_with_llm_response():
    return LLM_RESPONSE


@pytest.fixture
def llm_client_temp_input():
    return TEMP_PROMPT


@pytest.fixture
def llm_test_planning_request():
    return LLM_REQUEST


@pytest.fixture
def llm_client_with_invalid_llm_response():
    return INVALID_LLM_RESPONSE


@pytest.fixture
def llm_client_with_missing_field_llm_response():
    return LLM_RESPONSE_MISSING_FIELD


@pytest.fixture
def llm_client_with_list_llm_response():
    return LLM_RESPONSE_LIST


@pytest.fixture
def llm_response_with_nodict_nolist():
    return LLM_RESPONSE_WITH_NODICT_NOLIST
