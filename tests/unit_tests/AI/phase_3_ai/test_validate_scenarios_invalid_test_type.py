import pytest

from app.ai.response_parser import ResponseParser


def test_validate_scenarios_invalid_test_type(
    llm_client_with_llm_response,
    llm_swagger_endpoint,
):
    mock_response = llm_client_with_llm_response.copy()
    mock_response["test_type"] = "INVALID"

    rp = ResponseParser()

    with pytest.raises(ValueError, match="Invalid test type"):
        rp.validate_scenarios(mock_response, llm_swagger_endpoint)
