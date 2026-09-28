def test_resolve_schema_allof_skips_empty_part(
    resolver,
    schema_with_allof_empty_part,
    expected_allof_with_empty_part,
):
    result = resolver.resolve_schema_ref(
        schema_with_allof_empty_part,
        {},
    )

    assert result == expected_allof_with_empty_part
