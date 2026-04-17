from app.api_parser.swagger_parser import SwaggerParser
import json
 
def main():
    parser = SwaggerParser()
    endpoints = parser.parse_paths()
    print(json.dumps(endpoints, indent=4))



if __name__ == "__main__":
    main()