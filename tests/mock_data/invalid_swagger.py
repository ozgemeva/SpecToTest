
INVALID_SWAGGER_DATA = {
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