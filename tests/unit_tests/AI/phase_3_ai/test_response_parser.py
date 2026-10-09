import json

from app.ai.response_parser import ResponseParser


def test_response_parser(llm_client_with_llm_response):
    output_text = json.dumps(llm_client_with_llm_response)
    rp = ResponseParser()
    result = rp.parse_response(output_text)

    assert result == llm_client_with_llm_response
