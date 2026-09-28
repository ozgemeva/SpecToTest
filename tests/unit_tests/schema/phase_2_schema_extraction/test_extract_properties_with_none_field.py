from app.schema.schema_extractor import SchemaExtractor


def test_extract_properties_with_none_field(schema_properties_with_none_field):
    schExt = SchemaExtractor()
    result = schExt.extract_properties_metadata(schema_properties_with_none_field)

    assert "type" not in result["id"]
    assert "format" not in result["id"]
    assert "enum" not in result["status"]
    assert "type" not in result["tags"]
