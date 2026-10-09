from app.ai.response_parser import ResponseParser


def test_validate_scenarios_single_dict(llm_client_with_llm_response):
    rp = ResponseParser()
    rp.validate_scenarios(llm_client_with_llm_response)
