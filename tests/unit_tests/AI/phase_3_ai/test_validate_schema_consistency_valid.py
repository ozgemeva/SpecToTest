from app.ai.response_parser import ResponseParser


def test_validate_schema_consistency_valid(
    llm_client_with_llm_response, llm_swagger_endpoint
):

    rp = ResponseParser()
    rp.validate_schema_consistency(llm_client_with_llm_response, llm_swagger_endpoint)
