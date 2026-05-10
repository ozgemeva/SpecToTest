
#mock test with mock data (isolation) test do not affected by the internet.
VALID_SWAGGER_DATA= { 
        "paths": {
            "/test": {
                "get": {
                    "summary": "Test endpoint",
                    "operationId": "getTest",
                    "tags": ["test"]
                }
            },
            "/user": {
                "post": {
                    "summary": "Create user",
                    "operationId": "createUser",
                    "tags": ["user"]
                }
            }
        }
    }