import json


# Converts the AI output string into a Python object.
class ResponseParser:
    def parse_response(self, output_text):
        json_resp = json.loads(output_text)
        return json_resp

    def validate(self, parsed_response):
        self.validate_response(parsed_response)
        self.validate_response_type(parsed_response)
    
    def validate_response(self, parsed_response):
        required_fields = [
            "scenario_name",
            "test_type",
            "target",
            "rule",
            "endpoint",
            "http_method",
            "path_params",
            "query_params",
            "request_body",
            "expected_status",
            "expected_result",
        ]
        for field in required_fields:
            if field not in parsed_response:
                raise ValueError(f"Missing required field: {field}")
            
    def validate_response_type(self, parsed_response):
        expected_types = {
            "scenario_name": str,
            "test_type": str,
            "target": str,
            "rule": str,
            "endpoint": str,
            "http_method": str,
            "path_params": dict,
            "query_params": dict,
            "request_body": dict,
            "expected_status": int,
            "expected_result": str,
        }
        for field, expected_type in expected_types.items():
            if not isinstance(parsed_response[field], expected_type):
               raise TypeError(f"Invalid type for {field}")
    
# Validate each scenario individually using the same rules.
    def validate_scenarios(self, parsed_response):
        # A single test scenario is represented as a dictionary.
        if isinstance(parsed_response, dict):
            self.validate(parsed_response)
    
        # Multiple test scenarios are represented as a list.
        elif isinstance(parsed_response, list):
            for scenario in parsed_response:
                self.validate(scenario)
                
         # Reject unexpected response formats. 
        else:
            raise TypeError("Response must be a dict or list")
            
        