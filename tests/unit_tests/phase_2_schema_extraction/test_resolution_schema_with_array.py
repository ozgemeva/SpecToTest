from app.schema.schema_resolver import SchemaResolver


def test_resolution_schema_with_array(
    schema_array_with_item_ref, swagger_with_pet_definition
):
    sr = SchemaResolver()
    result = sr.resolve_schema_ref(
        schema_array_with_item_ref, swagger_with_pet_definition
    )

    # Verifies that an array schema resolves $ref from its items definition.
    assert result == swagger_with_pet_definition["definitions"]["Pet"]
