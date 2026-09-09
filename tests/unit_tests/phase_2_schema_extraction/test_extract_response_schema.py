from app.api_parser.swagger_parser import SwaggerParser


def test_extract_response_schema(swagger_body_paramete_response_schema_detail_data):
    parser = SwaggerParser()
    result = parser.extract_response_schema(
        swagger_body_paramete_response_schema_detail_data
    )

    assert result == {
        "$ref": "#/definitions/User"
    }, "Expected response schema to be extracted from Swagger 200 response"
