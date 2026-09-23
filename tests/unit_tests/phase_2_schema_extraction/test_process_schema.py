from app.schema.schema_processor import SchemaProcessor


def test_process_schema_returns_none_when_schema_empty(schema_process_empty_schema):
    sp = SchemaProcessor()
    result = sp.process_schema(schema_process_empty_schema, {})

    assert result is None
