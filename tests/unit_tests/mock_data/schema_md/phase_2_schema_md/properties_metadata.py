PROPERTIES_METADATA_WITHOUT_REQUIRED = {
    "type": "object",
    "properties": {
        "id": {"type": "integer", "format": "int64"},
        "status": {"type": "string", "enum": ["placed", "approved", "delivered"]},
    },
}

PROPERTIES_METADATA_WITH_REQUIRED = {
    "type": "object",
    "required": ["id"],
    "properties": {
        "id": {"type": "integer", "format": "int64"},
        "status": {"type": "string", "enum": ["placed", "approved", "delivered"]},
    },
}

PROPERTIES_METADATA = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
            "format": "int64",
            "example": 123,
        },
        "status": {
            "type": "string",
            "enum": ["placed", "approved", "delivered"],
            "example": "placed",
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "category": {
            "$ref": "#/definitions/Category",
        },
    },
}

PROPERTIES_METADATA_NONE_FIELD = {
    "type": "object",
    "properties": {
        "id": {
            "type": None,
            "format": None,
            "example": 123,
        },
        "status": {
            "type": "string",
            "enum": None,
            "example": "placed",
        },
        "tags": {
            "type": None,
            "items": {
                "type": "string",
            },
        },
        "category": {
            "$ref": "#/definitions/Category",
        },
    },
}

NESTED_REFERENCE_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "category": {"$ref": "#/definitions/Category"},
    },
}

SWAGGER_WITH_CATEGORY_DEFINITION = {
    "definitions": {
        "Category": {
            "type": "object",
            "properties": {"id": {"type": "integer"}, "name": {"type": "string"}},
        }
    }
}
