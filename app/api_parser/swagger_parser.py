# This parser expects Swagger/OpenAPI format
import requests
from app.config import Config
import json


class SwaggerParser:
    VALID_METHODS = {"get", "post", "put", "delete", "patch"}

    def __init__(self):
        self.url = Config.SWAGGER_URL  # "https://petstore.swagger.io/v2/swagger.json"
        self.source = Config.LOCAL_SWAGGER_FILE  # "spec/petstore.json"

    def fetch_swagger(self):
        try:
             
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()  # 200 OK,404 NOTFOUND,500 ServerError
            return response.json()

        except requests.RequestException as e:
            print(f"Failed to fetch from URL: {e}")
            print("Falling back to local Swagger file...")
            return self.fetch_swagger_from_file(self.source)

    def fetch_swagger_from_file(self, file_source):
        with open(file_source, "r") as file:
            return json.load(file)

    def parse_paths(self):
        swagger_data = self.fetch_swagger()  # to take json

        if "paths" not in swagger_data:  # json paths key
            raise ValueError("Invalid Swagger Format")

        if not isinstance(swagger_data["paths"], dict):
            raise ValueError("Paths must be a dictionary")

        paths = swagger_data["paths"]
        parsed_endpoints = []
        # print("paths.items:===>" , json.dumps(paths, indent=4))

        # for key, value in dict.items():
        for path, methods in paths.items():
            if not isinstance(methods, dict):
                raise ValueError("Methods must be a dictionary")
            # print("methods:===>" , json.dumps(methods, indent=4))

            for method, details in methods.items():
                if method.lower() not in self.VALID_METHODS:
                    continue

                if not isinstance(details, dict):
                    raise ValueError("Details must be a dictionary")

                parsed_endpoints.append(
                    {
                        "path": path,
                        "method": method.upper(),
                        "summary": details.get("summary", "No summary"),
                        "operation_id": details.get("operationId"),
                        "tags": details.get("tags", []),
                        "consumes": self.get_request_content_types(details),
                        "produces": self.get_response_content_types(details),
                        "request_schema": self.extract_request_schema(details),
                        "response_schema":self.extract_response_schema(details),
                    }
                )

                # print("details:===>" , json.dumps(details, indent=4))
        #print("parsed_endpoints:===>" , json.dumps(parsed_endpoints, indent=4))
        return parsed_endpoints

    def get_response_content_types(self, details):
        # Returns the response content types from "produces" for Swagger 2.0
        return details.get("produces", [])  #'produces': ['application/json'],

    def get_request_content_types(self, details):
        # Returns the request content types from "consumes" for Swagger 2.0
        return details.get("consumes", [])  #'consumes': ['multipart/form-data']

    def extract_request_schema(self, details):
        parameters = details.get("parameters", [])
        # print("parameters:===>" , json.dumps(parameters, indent=4))
        for parameter in parameters:
           # print("parameterForSchema:===>", json.dumps(parameter, indent=4))
            if parameter.get("in") == "body":
                return parameter.get("schema")
        return None

    def extract_response_schema(self, details):
        responses = details.get("responses", {})

        if not isinstance(responses, dict):
            return None

        response_data = responses.get("200")
        if not isinstance(response_data, dict):
            return None

        return response_data.get("schema")