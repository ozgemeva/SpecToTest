from app.schema.schema_extractor import SchemaExtractor


def test_extract_properties_type(schema_request_with_type):
    se = SchemaExtractor()
    result = se.extract_type(schema_request_with_type)
    assert result == "object"
