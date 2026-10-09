from app.ai.response_parser import ResponseParser


def test_validate_with_valid_response(llm_client_with_llm_response):
    rp = ResponseParser()
    rp.validate(llm_client_with_llm_response)