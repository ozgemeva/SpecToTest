import requests
from app.api_parser.swagger_parser import SwaggerParser
import pytest

def test_fetch_swagger_returns_json_from_url(mocker):
    mock_response=mocker.Mock()
    mock_response.raise_for_status.return_value = None
    
     
    mock_response.json.return_value = {"paths": {} }
    
    mocker.patch( "app.api_parser.swagger_parser.requests.get",return_value=mock_response )

    parser = SwaggerParser()

    result = parser.fetch_swagger()
    
    mock_response.raise_for_status.assert_called_once()
    mock_response.json.assert_called_once()

    assert result == {"paths": {}}

    