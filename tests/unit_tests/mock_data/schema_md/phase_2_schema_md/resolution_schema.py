ARRAY_SCHEMA_WITH_ITEM_REF = {"type": "array", "items": {"$ref": "#/definitions/Pet"}}

SCHEMA_WITH_DIRECT_REF = {"$ref": "#/definitions/Pet"}

SWAGGER_WITH_PET_DEFINITION = {
    "definitions": {
        "Pet": {"type": "object", "properties": {"id": {"type": "integer"}}}
    }
}

SCHEMA_WITHOUT_REF = {"type": "object", "properties": {"id": {"type": "integer"}}}

SCHEMA_WITH_ALLOF = {
    "allOf": [
        {
            "type": "object",
            "required": ["id", "name"],
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
            },
        },
        {
            "type": "object",
            "required": ["name", "status"],
            "properties": {
                "name": {"type": "string"},
                "status": {"type": "string"},
            },
        },
    ]
}

EXPECTED_ALLOF_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "status"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "status": {"type": "string"},
    },
}

SCHEMA_WITH_ALLOF_EMPTY_PART = {
    "allOf": [
        {},
        {
            "type": "object",
            "required": ["id"],
            "properties": {
                "id": {"type": "integer"},
            },
        },
    ]
}

EXPECTED_ALLOF_WITH_EMPTY_PART = {
    "type": "object",
    "required": ["id"],
    "properties": {
        "id": {"type": "integer"},
    },
}

SCHEMA_WITH_UNKNOWN_REF = {"$ref": "#/definitions/UnknownModel"}

SWAGGER_WITHOUT_REFERENCED_DEFINITION = {"definitions": {}}
