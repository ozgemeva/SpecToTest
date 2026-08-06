# This parser expects Swagger/OpenAPI format
import json

import requests

from app.config import Config


class SwaggerParser:
    VALID_METHODS = {"get", "post", "put", "delete", "patch"}

    def __init__(
        self,
        url=Config.SWAGGER_URL,  # "https://petstore.swagger.io/v2/swagger.json"
        source=Config.LOCAL_SWAGGER_FILE,  # "spec/petstore.json"
        timeout=Config.REQUEST_TIMEOUT,
    ):
        self.url = url
        self.source = source
        self.timeout = timeout

    def fetch_swagger(self):
        try:

            response = requests.get(self.url, self.timeout)
            response.raise_for_status()  # 200 OK,404 NOTFOUND,500 ServerError
            return response.json()

        except requests.RequestException as exc:
            print(f"Failed to fetch from {self.url}: {exc}")
            print("Falling back to local Swagger file {self.source}")
            return self.fetch_swagger_from_file(self.source)

    def fetch_swagger_from_file(self, file_source):
        try:
            with open(file_source, encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"Local Swagger file not found: {file_source}"
            ) from exc
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Local Swagger file contains invalid JSON: {file_source}"
            ) from exc

    def parse_paths(self):
        swagger_data = self.fetch_swagger()  # to take json

        if "paths" not in swagger_data:  # json paths key
            raise ValueError("Invalid Swagger document: missing 'paths' field")

        if not isinstance(swagger_data["paths"], dict):
            raise ValueError("Invalid Swagger document: 'paths' must be a dictionary")

        paths = swagger_data["paths"]
        parsed_endpoints = []
        # print("paths.items:===>" , json.dumps(paths, indent=4))

        # for key, value in dict.items():
        for path, methods in paths.items():
            if not isinstance(methods, dict):
                raise ValueError(
                    f"Invalid path definition for '{path}': expected a dictionary"
                )
            # print("methods:===>" , json.dumps(methods, indent=4))

            for method, details in methods.items():
                if method.lower() not in self.VALID_METHODS:
                    continue

                if not isinstance(details, dict):
                    raise ValueError(
                        f"Invalid operation '{method}' for path '{path}': "
                        "expected a dictionary"
                    )

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
                        "response_schema": self.extract_response_schema(details),
                    }
                )

                # print("details:===>" , json.dumps(details, indent=4))
        # print("parsed_endpoints:===>" , json.dumps(parsed_endpoints, indent=4))
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
