
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

EMPTY_INVALID_SWAGGER_DATA = {}

ISDICT_INVALID_SWAGGER_DATA ={
   "paths":""
}

ISDICT_INVALID_MEHTOD_SWAGGER_DATA ={
  "paths": {
            "/test":"invalid"
            }
}