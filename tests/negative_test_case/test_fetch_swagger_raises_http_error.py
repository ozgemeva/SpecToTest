import pytest 
import requests
from app.api_parser.swagger_parser import SwaggerParser

@pytest.mark.parametrize( "error_message", [ "401 Unauthorized", 
                                               "404 Not Found", 
                                               "500 Server Error" ] )
def test_fetch_swagger_raises_http_error( mocker, error_message ):
        mock_response = mocker.Mock()
        
        # simulate status code error 
        #to defined status code with side_effect()
        mock_response.raise_for_status.side_effect = ( requests.HTTPError(error_message) ) 

        mocker.patch( "app.api_parser.swagger_parser.requests.get", return_value=mock_response )  
        parser = SwaggerParser()
    
        print ("mock_response: ",mock_response.raise_for_status.side_effect )

        with pytest.raises(requests.HTTPError): 
          
            parser.fetch_swagger()