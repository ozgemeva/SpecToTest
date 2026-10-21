import json

import pytest

from app.ai.response_parser import ResponseParser


# Verify that ResponseParser raises JSONDecodeError
# when the LLM response contains invalid JSON.
def test_parse_response_raises_error_for_invalid_json(
    llm_client_with_invalid_llm_response,
):
    rp = ResponseParser()
    with pytest.raises(json.JSONDecodeError):
        rp.parse_response(llm_client_with_invalid_llm_response)
