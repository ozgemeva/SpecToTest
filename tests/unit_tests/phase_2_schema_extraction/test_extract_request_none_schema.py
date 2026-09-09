from app.api_parser.swagger_parser import SwaggerParser


def test_extract_request_schema_when_body_parameter_missing(swagger_body_parameter_request_schema_none_details_data):
    parser = SwaggerParser()
    result = parser.extract_request_schema(swagger_body_parameter_request_schema_none_details_data)
    assert result is None, "Expected None when Swagger body parameter does not exist"
