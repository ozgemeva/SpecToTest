import pytest

from app.ai.response_parser import ResponseParser


# Verify that validate_scenarios raises TypeError
# when the parsed LLM response is neither a dict nor a list.
def test_validate_scenarios_no_dict_list(llm_response_with_nodict_nolist):
    rp = ResponseParser()

    with pytest.raises(TypeError):
        rp.validate_scenarios(llm_response_with_nodict_nolist)
