REQUEST_SCHEMA_DETAILS_DATA = {
    "parameters": [
        {"name": "username", "in": "path", "type": "string"},
        {"name": "body", "in": "body", "schema": {"$ref": "#/definitions/User"}},
    ]
}

REQUEST_SCHEMA_NONE_DETAILS_DATA = {
    "parameters": [
        {"name": "username", "in": "path", "type": "string"},
        {"name": "body", "in": "xxx", "schema": {"$ref": "#/definitions/User"}},
    ]
}

SCHEMA_WITH_TYPE = {"type": "object"}

SCHEMA_WITH_PROPERTIES = {"properties": {}}
