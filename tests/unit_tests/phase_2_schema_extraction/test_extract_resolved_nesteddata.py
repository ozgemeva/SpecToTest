from app.schema.schema_extractor import SchemaExtractor
from app.schema.schema_resolver import SchemaResolver


def test_resolve_nested_references(
    schema_with_nested_reference,
    swagger_with_category_definition,
):
    se = SchemaExtractor()
    sr = SchemaResolver()

    result = se.resolve_nested_references(
        schema_with_nested_reference,
        swagger_with_category_definition,
        sr,
    )

    assert (
        result["category"]
        == swagger_with_category_definition["definitions"]["Category"]
    )
