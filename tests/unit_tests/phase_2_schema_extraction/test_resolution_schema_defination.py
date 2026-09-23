from app.schema.schema_resolver import SchemaResolver


def test_resolution_schema_defination(swagger_with_pet_definition):
    sr = SchemaResolver()
    result = sr.get_definitions(swagger_with_pet_definition)

    assert result == swagger_with_pet_definition["definitions"]
