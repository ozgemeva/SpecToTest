from app.schema.schema_resolver import SchemaResolver


def test_resolve_schema_with_allof(
    schema_with_allof,
    expected_allof_schema,
):
    resolver = SchemaResolver()

    result = resolver.resolve_schema_ref(
        schema_with_allof,
        {},
    )

    assert result == expected_allof_schema