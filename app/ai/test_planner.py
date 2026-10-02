import json


class BuildTestPlan:
    # Builds the prompt used as input for the LLM.
    def build_test_planning_prompt(self, endpoint, request_schema, response_schema):

        inst_prompt = self.build_task_instructions()
        output_prompt = self.build_output_format()
        data_for_prompt = self.build_test_input_data(
            endpoint, request_schema, response_schema
        )

        prompt = f"""
        {inst_prompt}
        {data_for_prompt}
        {output_prompt}
        """
        
        return prompt

    def build_output_format(self):

        output_prompt = """
                1. Return the generated test scenarios as structured JSON.
                2. Each test scenario should contain: scenario_name, test_type,
                target, rule, endpoint, http_method, path_params, query_params,
                request_body, expected_status, and expected_result."""

        return output_prompt

    def build_task_instructions(self):
        inst_prompt = """
        
                Generate API test scenarios using the API information provided below.
                Instructions:
                1. Use the provided API endpoint and HTTP method.
                2. Use the request schema metadata to generate test scenarios for the request data.
                3. Use the response schema metadata to generate test scenarios for validating the expected API response.
                4. Generate positive, negative,and edge test scenarios based on the provided schema rules.
                5. Use only the rules defined in the API specification. 
                Do not invent unsupported business rules or constraints.
                """

        return inst_prompt

    def build_test_input_data(self, endpoint, request_schema, response_schema):

        data = {
            "endpoint": endpoint,
            "request_schema": request_schema,
            "response_schema": response_schema,
        }

        input_data = json.dumps(data, indent=4)
        return input_data
