# This parser expects Swagger/OpenAPI format
import requests
from app.config import Config
import json

class SwaggerParser:
    VALID_METHODS = {"get", "post", "put", "delete", "patch"}

    def __init__(self):
        self.url=Config.SWAGGER_URL
        self.source =Config.LOCAL_SWAGGER_FILE
        
    def fetch_swagger(self):
        if self.source.startswith("http"):
         response = requests.get(self.url, timeout=10)
         response.raise_for_status() #200 OK,404 NOTFOUND,500 ServerError
         return response.json()
       
        else:
           return self.fetch_swagger_from_file(self.source)
    
    def fetch_swagger_from_file(self, file_source):
        with open(file_source, "r") as file:
            return json.load(file)
    
    def get_request_content_types(self, details):
        
        return self.request_content_types
    
    def parse_paths(self):
        swagger_data = self.fetch_swagger()#to take json
        
        if swagger_data.get("swagger"):
            print("\nWorking type is Swagger 2.0")
        elif swagger_data.get("openapi"):
            print("\n Working type is OpenAPI 3")
        
        if "paths" not in swagger_data: #json paths key
            raise ValueError("Invalid Swagger Format")
    
        if not isinstance(swagger_data["paths"],dict):
            raise ValueError("Paths must be a dictionary")
        
        paths = swagger_data["paths"]
        parsed_endpoints = []
       # print("paths.items:===>" , json.dumps(paths, indent=4))
       
        #for key, value in dict.items():
        for path, methods in paths.items():
         if not isinstance(methods,dict):
            raise ValueError("Methods must be a dictionary")
        # print("methods:===>" , json.dumps(methods, indent=4))
        
         for method, details in methods.items():   
                if method.lower() not in self.VALID_METHODS:
                    continue
                   
                if not isinstance(details, dict):
                    raise ValueError("Details must be a dictionary")

                self.get_response_content_types(details)
                self.get_request_content_types(details)
                
                parsed_endpoints.append({ "path": path, "method": method.upper(), 
                                         "summary": details.get("summary", "No summary"), 
                                         "operation_id": details.get("operationId"), 
                                         "tags": details.get("tags", []),
                                         "requestBody": self.get_request_content_types(details),
                                         "responses": self.get_response_content_types(details)})
                
               # print("details:===>" , json.dumps(details, indent=4))
       
        return parsed_endpoints

    def get_response_content_types(self, details):
         response_content_types = []

         for response_data in details.get("responses", {}).values():
            response_content_types.extend(
            response_data.get("content", {}).keys() )
            return list(set(response_content_types))
            

    def get_request_content_types(self, details):
        request_content_types = list (details.get("requestBody", {})
                                      .get("content", {}) 
                                      .keys())
        return request_content_types
    