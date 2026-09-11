from app.schema.schema_extractor import SchemaExtractor


def test_extract_properties_with_required(schema_properties_wit_required):
    schExt = SchemaExtractor()
    result = schExt.extract_properties_metadata(schema_properties_wit_required)

    assert result["id"]["required"] is True
    assert result["status"]["required"] is False
