# This parser expects Swagger/OpenAPI format
import requests
import json
from app.config import Config


class SwaggerParser:
    def __init__(self):
        self.url=Config.SWAGGER_URL
        
    def fetch_swagger(self):
        response = requests.get(self.url)
        response.raise_for_status() #200 OK,404 NOTFOUND,500 ServerError
        return response.json()
    
    
    
    def parse_paths(self):
        swagger_data = self.fetch_swagger()
        paths = swagger_data.get("paths", {}) #if there is paths return paths or if there is not parse return {}dict 
        parsed_endpoints = []
        VALID_METHODS = {"get", "post", "put", "delete", "patch"}
        
        if "paths" not in swagger_data:
            raise ValueError("Invalid Swagger format")
       
        for path, methods in paths.items():
            for method, details in methods.items():   
                if method.lower() not in VALID_METHODS:
                    continue
                if not isinstance(details, dict):
                    continue
                parsed_endpoints.append({
                    "path": path,
                    "method": method.upper(),
                    "summary": details.get("summary", "No summary"),
                    "operation_id": details.get("operationId"),
                    "tags": details.get("tags", [])})
        return parsed_endpoints
        