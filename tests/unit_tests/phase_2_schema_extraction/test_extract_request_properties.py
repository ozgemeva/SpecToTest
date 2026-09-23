from app.schema.schema_extractor import SchemaExtractor


def test_extract_request_properties(schema_request_with_properties):
    se = SchemaExtractor()
    result = se.extract_properties(schema_request_with_properties)
    assert result == {}
