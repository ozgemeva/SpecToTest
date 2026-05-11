import pytest
import json

def test_empty_paths_returns_empty_list(parser_with_empty_paths_mock):
    endpoints = parser_with_empty_paths_mock.parse_paths()
    
    print("<--endpoints-->\n",json.dumps(endpoints, indent=4))
    assert endpoints == [], ("Expected empty endpoint list for empty paths")

    