import pytest

from app.ai.response_parser import ResponseParser


# Verify that validate_response raises ValueError
# when a required field is missing from the LLM response.
def test_validate_response_raises_error_for_missing_field(
    llm_client_with_missing_field_llm_response,
):
    rp = ResponseParser()
    with pytest.raises(ValueError):
        rp.validate_response(llm_client_with_missing_field_llm_response)
