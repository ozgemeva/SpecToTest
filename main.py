from app.ai.test_planner import BuildTestPlan
from app.api_parser.swagger_parser import SwaggerParser
from app.schema.schema_processor import SchemaProcessor


def main():
    parser = SwaggerParser()
    processor = SchemaProcessor()
    ai_test_prompt = BuildTestPlan()

    swagger_data = parser.fetch_swagger()
    endpoints = parser.parse_paths()

    for endpoint in endpoints:
        # Process request and response schemas for the current endpoint.
        request_result = processor.process_schema(
            endpoint["request_schema"],
            swagger_data,
        )

        response_result = processor.process_schema(
            endpoint["response_schema"],
            swagger_data,
        )
        
        # its processed request/response schema metadata.
        # if request_result:
        #     print("REQUEST")
        #     print(json.dumps(request_result, indent=4))

        # if response_result:
        #     print("RESPONSE")
        #     print(json.dumps(response_result, indent=4))

        # Build the LLM prompt using the endpoint and
        # its processed request/response schema metadata.
        ai_result = ai_test_prompt.build_test_planning_prompt(
            endpoint,
            request_result,
            response_result,
        )

        # Print the complete prompt to verify the data
        # before sending it to the LLM.
        if ai_result:
            print("AI PROMPT")
            print(ai_result)

            # TEMPORARY: Process only the first endpoint
            # while testing the initial LLM integration.
            break


if __name__ == "__main__":
    main()