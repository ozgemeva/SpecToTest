from app.api_parser.swagger_parser import SwaggerParser


def test_extract_response_schema_when_responses_not_dict(
    schema_response_body_parameter_nondict_detais_data,
):
    parser = SwaggerParser()
    result = parser.extract_response_schema(
        schema_response_body_parameter_nondict_detais_data
    )
    assert (
        result is None
    ), "Expected None when Swagger response body parameter is not dictionary"
