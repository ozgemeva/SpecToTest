from app.api_parser.swagger_parser import SwaggerParser


def test_extract_response_schema(schema_response_body_parameter_detail_data):
    parser = SwaggerParser()
    result = parser.extract_response_schema(schema_response_body_parameter_detail_data)

    assert result == {
        "$ref": "#/definitions/User"
    }, "Expected response schema to be extracted from Swagger 200 response"
