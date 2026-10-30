import pytest

from app.ai.response_parser import ResponseParser

def test_validate_schema_consistency_invalid_path(llm_client_with_llm_response,llm_swagger_endpoint):
    mock_response = llm_client_with_llm_response.copy()
    mock_response["endpoint"] = "/user"     
    rp = ResponseParser()
    
    with pytest.raises(ValueError,match="Path does not match Swagger Path"):
        rp.validate_schema_consistency(mock_response,llm_swagger_endpoint)
   