from app.api_parser.swagger_parser import SwaggerParser
import pytest

#pytest search in conftest for this swagger_body_parameter_details feature
def test_extract_request_schema(swagger_body_parameter_details):
    parser = SwaggerParser()
    result = parser.extract_request_schema(swagger_body_parameter_details)
    
    assert result == { "$ref": "#/definitions/User" },"Expected request schema to be extracted from Swagger body parameter"
    
    
