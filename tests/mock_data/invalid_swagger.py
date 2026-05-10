import pytest

@pytest.fixture
def invalid_swagger_data():
    return
    {
        "paths": {
            "/test": {
                "aaa": {
                    "summary": "Invalid method",
                    "operationId": "getTest",
                    "tags": ["test"]
                }
            },
            "/user": {
                "xxx": {
                    "summary": "invalid_Create user",
                    "operationId": "createUser",
                    "tags": ["user"]
                }
            }
        }
    } 