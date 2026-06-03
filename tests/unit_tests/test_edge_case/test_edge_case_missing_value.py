import pytest
import json

def test_edge_case_missing_value(parser_with_missing_fields_mock,):
  endpoints = parser_with_missing_fields_mock.parse_paths()
     
  #key_tuple=(ep["path"], ep["method"]), value : endpoints_fromParser.item()
  endpoint_map = {
                    (ep["path"], ep["method"]): ep 
                    for ep in endpoints 
                    }
  
  ep = endpoint_map.get(("/test", "GET"))
  print("<--endpoints-->\n",json.dumps(endpoints, indent=4))
  assert ep is not None
  assert ep["summary"] == "No summary"
  assert ep["operation_id"] is None
  assert ep["tags"] == []