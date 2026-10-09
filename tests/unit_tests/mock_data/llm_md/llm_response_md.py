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

INVALID_LLM_RESPONSE = """
{
    "scenario_name": "test",
    "test_type": "positive",
    "endpoint": "/pet",
    "http_method": "POST"
"""

LLM_RESPONSE_MISSING_FIELD = {
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

LLM_RESPONSE_LIST = [
    {
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
    },
    {
        "scenario_name": "Create pet without required name",
        "test_type": "negative",
        "target": "request_body",
        "rule": "Missing required field",
        "endpoint": "/pet",
        "http_method": "POST",
        "path_params": {},
        "query_params": {},
        "request_body": {
            "status": "available",
        },
        "expected_status": 400,
        "expected_result": "Request is rejected due to missing required field",
    },
    {
        "scenario_name": "Create pet with empty name",
        "test_type": "edge",
        "target": "request_body",
        "rule": "Empty string boundary case",
        "endpoint": "/pet",
        "http_method": "POST",
        "path_params": {},
        "query_params": {},
        "request_body": {
            "name": "",
            "status": "available",
        },
        "expected_status": 400,
        "expected_result": "Request is rejected due to empty name",
    },
]

LLM_RESPONSE_WITH_NODICT_NOLIST= "no dict,no list"
