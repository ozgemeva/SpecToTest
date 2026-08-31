import json

from app.api_parser.swagger_parser import SwaggerParser
from app.schema.schema_processor import SchemaProcessor


def main():
    parser = SwaggerParser()
    processor = SchemaProcessor()

    swagger_data = parser.fetch_swagger()
    endpoints = parser.parse_paths()

    for endpoint in endpoints:
        request_result = processor.process_schema(
            endpoint["request_schema"], swagger_data
        )
        response_result = processor.process_schema(
            endpoint["response_schema"], swagger_data
        )

        if request_result:
            print("REQUEST")
            print(json.dumps(request_result, indent=4))

        if response_result:
            print("RESPONSE")
            print(json.dumps(response_result, indent=4))


if __name__ == "__main__":
    main()
