
import pytest

from app.ai.llm_client import LlmClient


# Verify that LlmClient raises ValueError when the API key is missing or empty.
@pytest.mark.parametrize("api_key", [None, ""])
def test_llm_client_raises_error_when_api_key_missing(monkeypatch, api_key):
    monkeypatch.setattr(
        "app.ai.llm_client.os.getenv",
        lambda key: api_key,  # def fake_getenv(key): return None
    )

    with pytest.raises(ValueError):
        LlmClient()
