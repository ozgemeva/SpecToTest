def test_send_prompt(
    llm_client_with_mock, llm_client_temp_input, 
    llm_client_with_llm_response,
    monkeypatch
):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-test-key")
    result = llm_client_with_mock.send_prompt(llm_client_temp_input)
    assert result == llm_client_with_llm_response
