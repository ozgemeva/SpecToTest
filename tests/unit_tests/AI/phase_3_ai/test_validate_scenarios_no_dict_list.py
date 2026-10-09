import pytest
from app.ai.response_parser import ResponseParser


def test_validate_scenarios_no_dict_list(llm_response_with_nodict_nolist):
    rp = ResponseParser()
    
    with pytest.raises(TypeError):
        rp.validate_scenarios(llm_response_with_nodict_nolist)