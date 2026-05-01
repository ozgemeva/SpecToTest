import pytest
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

#happy test case 
@pytest.mark.parametrize("path,method,summary,operation_id,tags",[
     ("/test", "GET", "Test endpoint", "getTest", ["test"]), #testCase-1
     ("/user", "POST", "Create user", "createUser", ["user"]) #testCase-2,
])

def test_parse_paths_returns_endpoint(parser_with_mock,path,method,summary,operation_id,tags):
    endpoints_fromParser = parser_with_mock.parse_paths() #list, parse_paths() in swagger_parser class  
    print(endpoints_fromParser)
    
    #key_tuple=(ep["path"], ep["method"]), value : endpoints_fromParser.item()
    endpoint_map = {
                    (ep["path"], ep["method"]): ep 
                    for ep in endpoints_fromParser 
                    }
    
    ep = endpoint_map.get((path, method))
    assert ep is not None
    assert ep["summary"] == summary
    assert ep["operation_id"] == operation_id
    assert ep["tags"] == tags
   