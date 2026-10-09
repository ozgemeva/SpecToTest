from app.ai.response_parser import ResponseParser


def test_validate_scenarios(llm_client_with_list_llm_response):
    rp = ResponseParser()
    result = rp.validate_scenarios(llm_client_with_list_llm_response)
    
    assert result is None
    