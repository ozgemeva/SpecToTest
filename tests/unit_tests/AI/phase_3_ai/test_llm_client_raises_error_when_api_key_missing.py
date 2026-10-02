import pytest

from app.ai.llm_client import LlmClient


def test_llm_client_raises_error_when_api_key_missing(monkeypatch):
    monkeypatch.setattr(
        "app.ai.llm_client.os.getenv",
        lambda key: None, #def fake_getenv(key): return None
    )

    with pytest.raises(ValueError):
        LlmClient()
