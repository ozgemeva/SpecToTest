import pytest
from app.ai.response_parser import ResponseParser

@pytest.mark.parametrize(
    "test_type",
    ["positive", "negative", "edge"])

def test_validate_response_values_valid_test_type(llm_client_with_llm_response, test_type):
    mock_response = llm_client_with_llm_response.copy()
    mock_response["test_type"] = test_type
    rp = ResponseParser()
    rp.validate_response_values(mock_response)