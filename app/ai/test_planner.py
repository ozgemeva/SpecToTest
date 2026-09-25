import json


class BuildTestPlan:

    def build_test_planning_prompt(self, endpoint, request_schema, response_schema):
        prompt = f"""
        Generate API test scenarios using the API information provided below.

        Instructions:
        1. Use the provided API endpoint and HTTP method.
        2. Use the request schema metadata to generate test scenarios
        for the request data.
        3. Use the response schema metadata to generate test scenarios
        for validating the expected API response.
        4. Generate positive, negative, 
        and edge test scenarios based on the provided schema rules.
        5. Use only the rules defined in the API specification. 
        Do not invent unsupported business rules or constraints.
        6. Return the generated test scenarios as structured JSON.
        7. Each test scenario should contain: scenario_name, test_type,
        target, rule, endpoint, http_method, path_params, query_params,
        request_body, expected_status, and expected_result.
        
        API endpoint:
        {json.dumps(endpoint, indent=4)}

        request schema metadata:
        {json.dumps(request_schema, indent=4)}

        response schema metadata:
        {json.dumps(response_schema, indent=4)}
        """

        print(prompt)
        return prompt
