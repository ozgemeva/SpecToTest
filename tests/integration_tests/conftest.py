import pytest

from app.ai.llm_client import LlmClient
from tests.mock_data.llm_md.llm_response_md import (
    INVALID_LLM_RESPONSE,
    INVALID_SCENARIO_RESPONSE,
    LLM_RESPONSE,
)
from tests.mock_data.llm_md.swagger_endpoint_md import MOCK_ENDPOINT


@pytest.fixture
def mock_llm(monkeypatch):
    received_prompts = []

    def setup(response):
        def fake_send_prompt(self, prompt):
            received_prompts.append(prompt)
            return response

        monkeypatch.setattr(
            LlmClient,
            "send_prompt",
            fake_send_prompt,
        )

        return received_prompts

    return setup


@pytest.fixture
def intg_llm_client_with_llm_response():
    return LLM_RESPONSE


@pytest.fixture
def intg_llm_swagger_endpoint():
    return MOCK_ENDPOINT


@pytest.fixture
def intg_llm_client_with_invalid_llm_response():
    return INVALID_LLM_RESPONSE


@pytest.fixture
def intg_llm_client_with_invalid_scenario_response():
    return INVALID_SCENARIO_RESPONSE
