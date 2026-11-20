
import json
import pytest

from app.ai.llm_client import LlmClient
from app.ai.response_parser import ResponseParser
from app.ai.test_planner import BuildTestPlan


def test_mock_llm_integration(
    mock_llm,
    intg_llm_client_with_llm_response,
    intg_llm_swagger_endpoint,
):
    received_prompts = mock_llm(
        json.dumps(intg_llm_client_with_llm_response)
    )

    prompt = BuildTestPlan().build_test_planning_prompt(
        intg_llm_swagger_endpoint, {}, {}
    )

    llm_output = LlmClient.send_prompt(None, prompt)
    parser = ResponseParser()
    parsed_response = parser.parse_response(llm_output)

    parser.validate_scenarios(
        parsed_response, intg_llm_swagger_endpoint
    )

    assert "/pet" in prompt
    assert "POST" in prompt
    assert received_prompts == [prompt]
    assert parsed_response == intg_llm_client_with_llm_response


def test_mock_llm_integration_invalid_json(
    mock_llm,
    intg_llm_client_with_invalid_llm_response,
):
    mock_llm(intg_llm_client_with_invalid_llm_response)

    llm_output = LlmClient.send_prompt(None, "POST /pet")

    with pytest.raises(json.JSONDecodeError):
        ResponseParser().parse_response(llm_output)


def test_mock_llm_integration_invalid_scenario(
    mock_llm,
    intg_llm_client_with_invalid_scenario_response,
    intg_llm_swagger_endpoint,
):
    received_prompts = mock_llm(
        json.dumps(intg_llm_client_with_invalid_scenario_response)
    )

    prompt = BuildTestPlan().build_test_planning_prompt(
        intg_llm_swagger_endpoint, {}, {}
    )

    llm_output = LlmClient.send_prompt(None, prompt)
    parsed_response = ResponseParser().parse_response(llm_output)

    with pytest.raises(ValueError):
        ResponseParser().validate_scenarios(
            parsed_response, intg_llm_swagger_endpoint
        )

    assert received_prompts == [prompt]
    assert parsed_response == intg_llm_client_with_invalid_scenario_response
