import pytest
from app.ai.llm_client import LlmClient
from tests.unit_tests.mock_data.llm_md.llm_response_md import (LLM_RESPONSE,TEMP_PROMPT,)
from types import SimpleNamespace

#cteate fake client for OpenAI
def create_mock_llm_client(monkeypatch, mock_data):
    llm_client = LlmClient()

#create fake responses.output
    def fake_create(**kwargs):
        return SimpleNamespace(output_text=mock_data)

#during test, we use fake_create method instead of "self.client.responses.create()"
    monkeypatch.setattr(
        llm_client.client.responses,
        "create",
        fake_create,
    )
    return llm_client

@pytest.fixture
def llm_client_with_mock(monkeypatch, llm_client_with_llm_response):
    return create_mock_llm_client(monkeypatch, llm_client_with_llm_response)

@pytest.fixture
def llm_client_with_llm_response():
    return LLM_RESPONSE

@pytest.fixture
def llm_client_temp_input():
    return TEMP_PROMPT

