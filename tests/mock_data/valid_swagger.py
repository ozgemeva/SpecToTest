import pytest
from app.api_parser.swagger_parser import SwaggerParser


#mock test with mock data (isolation) test do not affected by the internet.
@pytest.fixture
def valid_swagger_data():
    return {
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