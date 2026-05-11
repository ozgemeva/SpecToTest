import pytest
import json

def test_edge_case_uppercase_method(parser_with_uppercase_method_mock):
    endpoints = parser_with_uppercase_method_mock.parse_paths()
    endpoint_map = {
                    (ep["path"], ep["method"]): ep 
                    for ep in endpoints 
                    }
  
    ep = endpoint_map.get(("/test", "GET"))
    assert ep is not None, "Endpoint not found"
    print("<--endpoints-->\n",json.dumps(endpoints, indent=4))
    assert ep["method"] == "GET"

    
    