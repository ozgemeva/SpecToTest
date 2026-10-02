from app.ai.test_planner import BuildTestPlan


def test_build_test_planning_prompt(llm_test_planning_request):
    variable = BuildTestPlan()

    endpoint = llm_test_planning_request["endpoint"]
    request_schema = llm_test_planning_request["request_schema"]
    response_schema = llm_test_planning_request["response_schema"]

    expected_input_data = variable.build_test_input_data(endpoint,request_schema,response_schema, )

    result = variable.build_test_planning_prompt(endpoint,request_schema,response_schema,)

    assert isinstance(result, str)
    assert endpoint["path"] in result
    assert endpoint["method"] in result
    assert "Generate API test scenarios" in result
    assert "Return the generated test scenarios as structured JSON." in result
    assert expected_input_data in result