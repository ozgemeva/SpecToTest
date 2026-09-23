from app.schema.schema_resolver import SchemaResolver


def test_resolution_schema_modelname(schema_with_direct_ref):
    sr = SchemaResolver()
    result = sr.get_model_name(schema_with_direct_ref["$ref"])

    assert result == "Pet"
