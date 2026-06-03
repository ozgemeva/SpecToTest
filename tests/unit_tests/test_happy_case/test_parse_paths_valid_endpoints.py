import pytest
import json

#happy test case 
@pytest.mark.parametrize("path,method,summary,operation_id,tags",[
     ("/test", "GET", "Test endpoint", "getTest", ["test"]), #testCase-1
     ("/user", "POST", "Create user", "createUser", ["user"]) #testCase-2,
])

def test_parse_paths_extracts_valid_endpoints(parser_with_valid_mock,path,method,summary,operation_id,tags):
    endpoints_from_parser = parser_with_valid_mock.parse_paths() #list, parse_paths() in swagger_parser class  

    
    #key_tuple=(ep["path"], ep["method"]), value : endpoints_from_parser.item()
    assert len(endpoints_from_parser) == 2
    endpoint_map = {
                    (ep["path"], ep["method"]): ep 
                    for ep in endpoints_from_parser 
                    }
    
    ep = endpoint_map.get((path, method))
    #print("<--endpoints-->\n",json.dumps(endpoints_from_parser, indent=4))

    assert ep is not None
    assert ep["summary"] == summary
    assert ep["operation_id"] == operation_id
    assert ep["tags"] == tags
   