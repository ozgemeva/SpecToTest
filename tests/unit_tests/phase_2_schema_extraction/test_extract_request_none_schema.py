from app.api_parser.swagger_parser import SwaggerParser


def test_extract_request_none_schema(swagger_body_parameter_none_details):
    parser = SwaggerParser()
    result = parser.extract_request_schema(swagger_body_parameter_none_details)
    assert result is None, "Expected None when Swagger body parameter does not exist"
