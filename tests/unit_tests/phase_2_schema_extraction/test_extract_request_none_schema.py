from app.api_parser.swagger_parser import SwaggerParser


def test_extract_request_schema_when_body_parameter_missing(
    schema_request_body_parameter_none_details_data,
):
    parser = SwaggerParser()
    result = parser.extract_request_schema(
        schema_request_body_parameter_none_details_data
    )
    assert result is None, "Expected None when Swagger body parameter does not exist"
