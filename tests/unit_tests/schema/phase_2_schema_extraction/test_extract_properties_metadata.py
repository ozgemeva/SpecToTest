from app.schema.schema_extractor import SchemaExtractor


def test_extract_properties_metadata(schema_properties_metadata):
    schExt = SchemaExtractor()
    result = schExt.extract_properties_metadata(schema_properties_metadata)

    assert result["id"]["type"] == "integer"
    assert result["id"]["format"] == "int64"
    assert result["id"]["example"] == 123
    assert result["status"]["enum"] == ["placed", "approved", "delivered"]
    assert result["status"]["example"] == "placed"
    assert result["tags"]["items"] == {"type": "string"}
    assert result["category"]["$ref"] == "#/definitions/Category"
