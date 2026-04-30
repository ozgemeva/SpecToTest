import pytest # type: ignore
from app.api_parser.swagger_parser import SwaggerParser

#mock test with mock data
@pytest.fixture
def fake_swagger_data():
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
    
@pytest.fixture # fake_swagger_data = fake_swagger_data() 
def parser_with_mock(monkeypatch, fake_swagger_data):
    def fake_fetch(self):
        return fake_swagger_data
  
    monkeypatch.setattr(SwaggerParser, "fetch_swagger", fake_fetch)
    return SwaggerParser() #return instance from SwaggerParser

#test parse_paths() in swagger_parser class

def test_parse_paths_returns_endpoint(parser_with_mock):

    endpoints = parser_with_mock.parse_paths() #list
    assert len(endpoints) == 2, f"Expected 2 endpoint but got {len(endpoints)}"
    
    ep = endpoints[0]
    print("endpoints:",endpoints)
    assert ep['path'] == "/test",f"Expected '/test' endpoint but got {ep['path']}"
    assert ep['method'] == "GET",f"Expected 'GET' endpoint but got {['method']}"
    assert ep['summary'] == "Test endpoint",f"Expected 'Test endpoint' endpoint but got {['summary']}"
    assert ep['operation_id'] == "getTest",f"Expected 'getTest' endpoint but got {['operation_id']}"
    assert ep["tags"] == ["test"], f"Expected ['user'] endpoint but got {ep['tags']}"
    
    ep = endpoints[1]
    assert ep['path'] == "/user",f"Expected '/user' endpoint but got {ep['path']}"
    assert ep['method'] == "POST",f"Expected 'POST' endpoint but got {['method']}"
    assert ep['summary'] == "Create user",f"Expected 'Create user' endpoint but got {['summary']}"
    assert ep['operation_id'] == "createUser",f"Expected 'createUser' endpoint but got {['operation_id']}"
    assert ep["tags"] == ["user"], f"Expected ['user'] endpoint but got {ep['tags']}"

