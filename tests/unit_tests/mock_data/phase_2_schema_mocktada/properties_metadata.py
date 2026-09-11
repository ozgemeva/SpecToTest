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
