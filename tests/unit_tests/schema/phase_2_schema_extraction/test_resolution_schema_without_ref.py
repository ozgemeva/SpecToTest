from app.schema.schema_resolver import SchemaResolver


def test_resolution_schema_without_ref(schema_without_ref):
    sr = SchemaResolver()
    result = sr.resolve_schema_ref(
        schema_without_ref,
        {},
    )

    assert result == schema_without_ref
