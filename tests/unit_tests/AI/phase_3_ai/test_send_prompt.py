def test_send_prompt(llm_client_with_mock, llm_client_temp_input, llm_client_with_llm_response):
    result = llm_client_with_mock.send_prompt(llm_client_temp_input)
    assert result == llm_client_with_llm_response
    