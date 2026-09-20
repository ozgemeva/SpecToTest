from app.schema.schema_resolver import SchemaResolver


def test_resolution_schema_ref(schema_with_direct_ref, swagger_with_pet_definition):
    sr = SchemaResolver()
    result = sr.resolve_schema_ref(schema_with_direct_ref, swagger_with_pet_definition)

    assert result == swagger_with_pet_definition["definitions"]["Pet"]
