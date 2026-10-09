import json

import pytest

from app.ai.response_parser import ResponseParser


def test_response_invalid_parser(llm_client_with_invalid_llm_response):
    rp = ResponseParser()
    with pytest.raises(json.JSONDecodeError):
        rp.parse_response(llm_client_with_invalid_llm_response)
