import pytest
import json

def test_edge_extra_unknown_fields(parser_with_extra_unknown_field_mock):
    endpoints = parser_with_extra_unknown_field_mock.parse_paths()
    endpoint_map = {
                    (ep["path"], ep["method"]): ep 
                    for ep in endpoints 
                    }
  
    ep = endpoint_map.get(("/test", "GET"))
    assert ep is not None, "Endpoint not found"
    assert ep["method"] == "GET"
    assert "randomField" not in ep,("randomField this tag unexpected")
    print("<--endpoints-->\n",json.dumps(endpoints, indent=4))
   
