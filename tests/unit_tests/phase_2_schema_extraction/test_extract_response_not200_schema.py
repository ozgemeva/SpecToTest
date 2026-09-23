from app.api_parser.swagger_parser import SwaggerParser


def test_extract_response_not200_schema(
    schema_response_body_parameter_not200_details_data,
):
    parser = SwaggerParser()
    result = parser.extract_response_schema(
        schema_response_body_parameter_not200_details_data
    )

    assert result is None, "Expected None when Swagger 200 response does not exist"
