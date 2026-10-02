TEMP_PROMPT = "Generate API test scenarios"

LLM_RESPONSE = {
    "scenario_name": "Create pet with valid data",
    "test_type": "positive",
    "target": "request_body",
    "rule": "Valid request body",
    "endpoint": "/pet",
    "http_method": "POST",
    "path_params": {},
    "query_params": {},
    "request_body": {
        "name": "Buddy",
        "status": "available",
    },
    "expected_status": 200,
    "expected_result": "Pet is created successfully",
}

LLM_REQUEST = {
    "endpoint": {
        "path": "/pet",
        "method": "POST",
        "summary": "Add a new pet to the store",
        "operation_id": "addPet",
        "tags": ["pet"],
        "consumes": ["application/json"],
        "produces": ["application/json"],
    },
    "request_schema": {
        "metadata": {
            "name": {
                "type": "string",
                "required": True,
            },
            "status": {
                "type": "string",
                "enum": ["available", "pending", "sold"],
                "required": False,
            },
        },
        "nested_references": {},
    },
    "response_schema": {
        "metadata": {
            "id": {
                "type": "integer",
                "format": "int64",
                "required": False,
            },
            "name": {
                "type": "string",
                "required": True,
            },
        },
        "nested_references": {},
    },
}
