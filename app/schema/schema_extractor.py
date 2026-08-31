class SchemaExtractor:

    def extract_type(self, schema):
        return schema.get("type")

    def extract_required(self, schema):
        return schema.get("required",[])
   
    def extract_properties(self, schema):
        return schema.get("properties", {})

    def extract_properties_metadata(self,schema):
        properties= self.extract_properties(schema)
        extracted_properties = {}
        required_fields = self.extract_required(schema)
    
        for property_name, property_details in properties.items():
            is_required = property_name in required_fields

            metadata = {
                "type": property_details.get("type"),
                "format": property_details.get("format"),
                "enum": property_details.get("enum"),
                "example": property_details.get("example"),
                "items": property_details.get("items"),
                "$ref": property_details.get("$ref"),
                "required": is_required,
            }
            
            extracted_properties[property_name] = {
                key: value
                for key, value in metadata.items()
                if value is not None
            }
                   
        return extracted_properties
 