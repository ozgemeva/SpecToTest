# Verifies that SchemaProcessor returns mocked metadata and nested references.
def test_process_schema_returns_metadata_and_nested_references(
    processor_with_schema_mock,
    schema_process,
    schema_process_expected_metadata,
    schema_process_expected_nested,
):

    result = processor_with_schema_mock.process_schema(
        schema_process,
        {},
    )

    assert result["metadata"] == schema_process_expected_metadata
    assert result["nested_references"] == schema_process_expected_nested
