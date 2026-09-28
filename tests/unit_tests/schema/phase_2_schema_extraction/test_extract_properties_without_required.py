from app.schema.schema_extractor import SchemaExtractor


def test_extract_properties_metadata_without_required(
    schema_properties_without_required,
):
    schEx = SchemaExtractor()
    result = schEx.extract_properties_metadata(schema_properties_without_required)

    for property_metadata in result.values():
        assert (
            property_metadata["required"] is False
        ), "Expected all properties to be optional when required is not defined"
