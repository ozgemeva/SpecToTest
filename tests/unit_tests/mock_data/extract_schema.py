REQUEST_SCHEMA_DETAILS_DATA = {
    "parameters": [
        {"name": "username", "in": "path", "type": "string"},
        {"name": "body", "in": "body", "schema": {"$ref": "#/definitions/User"}},
    ]
}
