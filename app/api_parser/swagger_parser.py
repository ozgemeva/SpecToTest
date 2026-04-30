# This parser expects Swagger/OpenAPI format
import requests
from app.config import Config


class SwaggerParser:
    VALID_METHODS = {"get", "post", "put", "delete", "patch"}

    def __init__(self):
        self.url=Config.SWAGGER_URL
        
    def fetch_swagger(self):
        response = requests.get(self.url, timeout=10)
        response.raise_for_status() #200 OK,404 NOTFOUND,500 ServerError
        return response.json()
    
    def parse_paths(self):
        swagger_data = self.fetch_swagger()#to take json
        
        if "paths" not in swagger_data: #json paths key
            raise ValueError("Invalid Swagger format")
    
        paths = swagger_data["paths"]
        parsed_endpoints = []
        
       
       #for key, value in dict.items():
        for path, methods in paths.items():
            for method, details in methods.items():   
                if method.lower() not in self.VALID_METHODS:
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
        