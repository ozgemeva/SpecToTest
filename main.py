from app.api_parser.swagger_parser import SwaggerParser
from app.schema.schema_extractor import SchemaExtractor
from app.schema.schema_resolver import SchemaResolver


def main():
    parser = SwaggerParser()
    resolver = SchemaResolver()
    extractor = SchemaExtractor()

    swagger_data = parser.fetch_swagger()
    endpoints = parser.parse_paths()

    for endpoint in endpoints[:2]:
        request_schema = endpoint["request_schema"]

        if request_schema:
            resolved = resolver.resolve_schema_ref(request_schema, swagger_data)
            extractor.extract_properties(resolved)
            definitions = resolver.get_definitions(swagger_data)

            for name in definitions.items():
                print("NAME:", name)
                # print(f\n"DETAILS:", json.dumps(details, indent=4))


"""for endpoint in endpoints[:2]:
print(f"Path: {endpoint['path']}")
print(f"Method: {endpoint['method']}")
print(f"Summary: {endpoint['summary']}")
print(f"Operation ID: {endpoint['operation_id']}")
print(f"Tags: {endpoint['tags']}")
print(f"Consumes: {endpoint['consumes']}")
print(f"Produces: {endpoint['produces']}")
print(f"request_schema: {endpoint['request_schema']}")
print(f"response_schema: {endpoint['response_schema']}")
print("-" * 40)
"""

if __name__ == "__main__":
    main()
