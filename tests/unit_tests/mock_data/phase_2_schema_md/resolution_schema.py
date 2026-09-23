ARRAY_SCHEMA_WITH_ITEM_REF = {"type": "array", "items": {"$ref": "#/definitions/Pet"}}

SCHEMA_WITH_DIRECT_REF = {"$ref": "#/definitions/Pet"}

SWAGGER_WITH_PET_DEFINITION = {
    "definitions": {
        "Pet": {"type": "object", "properties": {"id": {"type": "integer"}}}
    }
}

SCHEMA_WITHOUT_REF = {"type": "object", "properties": {"id": {"type": "integer"}}}
