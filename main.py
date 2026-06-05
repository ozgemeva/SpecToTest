from app.api_parser.swagger_parser import SwaggerParser
import json
 
def main():
    parser = SwaggerParser()
    endpoints = parser.parse_paths()
   
    #print(json.dumps(endpoints, indent=4))
    for endpoint in endpoints[:2]:
        print(f"Path: {endpoint['path']}")
        print(f"Method: {endpoint['method']}")
        print(f"Summary: {endpoint['summary']}")
        print(f"Operation ID: {endpoint['operation_id']}")
        print(f"Tags: {endpoint['tags']}")
        print(f"Consumes: {endpoint['consumes']}")
        print(f"Produces: {endpoint['produces']}")
        print("-" * 40)


if __name__ == "__main__":
    main()
    