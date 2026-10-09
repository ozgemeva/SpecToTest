from app.ai.response_parser import ResponseParser
import pytest

@pytest.mark.parametrize(
    "field, wrong_value",
    [
        ("scenario_name", 1234),
        ("http_method", 1234),
        ("expected_status", "xxx"),
    ],
)
def test_validate_response_wrong_type(llm_client_with_llm_response,field,wrong_value):
        response = llm_client_with_llm_response.copy()
        response[field] = wrong_value
        rp = ResponseParser()
        with pytest.raises(TypeError):
            rp.validate_response_type(response)

