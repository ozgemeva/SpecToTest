import pytest
from app.api_parser.swagger_parser import SwaggerParser
    
def test_fetch_swagger_returns_json(mocker):

    mock_response = mocker.Mock() # create fake obj.
   
    # prduction code return JSON so we will return mock json data for test
    mock_response.json.return_value = {"paths": {}} 
    
    mocker.patch( "requests.get",return_value=mock_response)
    parser = SwaggerParser()

    result = parser.fetch_swagger()
   
    mock_response.raise_for_status.assert_called_once()
    assert result == {"paths": {}}
