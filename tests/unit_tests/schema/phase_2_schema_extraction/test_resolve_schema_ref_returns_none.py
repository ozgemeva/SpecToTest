def test_resolve_schema_ref_returns_none_when_definition_not_found(
    resolver,
    schema_with_unknown_ref,
    swagger_without_referenced_definition,
):
    result = resolver.resolve_schema_ref(
        schema_with_unknown_ref,
        swagger_without_referenced_definition,
    )

    assert result is None