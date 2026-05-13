EDGE_CASE_SWAGGER_MISSING_DATA= { 
        "paths": {
            "/test": {
                "get": {}
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

EDGE_CASE_SWAGGER_PATHS_DATA= { 
        "paths": {}
    }

EDGE_CASE_SWAGGER_UPPERCASE_METHOD_DATA= { 
        "paths": {
            "/test": {
                "gEt": {
                    "summary": "Uppercase Method",
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

EDGE_CASE_SWAGGER_EXTRA_UNKNOWN_DATA = {
  "paths": {
            "/test": {
                "GET": {
                    "summary": "Unkown Field",
                    "operationId": "get",
                    "randomField": "abc",
                    "tags" : ["test"]
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