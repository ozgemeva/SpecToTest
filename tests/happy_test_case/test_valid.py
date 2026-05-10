import pytest

#happy test case 
@pytest.mark.parametrize("path,method,summary,operation_id,tags",[
     ("/test", "GET", "Test endpoint", "getTest", ["test"]), #testCase-1
     ("/user", "POST", "Create user", "createUser", ["user"]) #testCase-2,
])

def test_parse_paths_returns_endpoint(parser_with_valid_mock,path,method,summary,operation_id,tags):
    endpoints_fromParser = parser_with_valid_mock.parse_paths() #list, parse_paths() in swagger_parser class  
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
   
    