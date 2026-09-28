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
