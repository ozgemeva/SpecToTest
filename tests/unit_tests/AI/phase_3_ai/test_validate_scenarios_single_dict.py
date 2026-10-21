from app.ai.response_parser import ResponseParser


# Verify that a single valid LLM test scenario (dict)
# passes validation without raising an exception.
def test_validate_scenarios_single_dict(llm_client_with_llm_response):
    rp = ResponseParser()
    rp.validate_scenarios(llm_client_with_llm_response)
