"""Extracts schema properties and test-relevant metadata
such as type, format, enum, example, items, and required fields."""


class SchemaExtractor:

    def extract_type(self, schema):
        return schema.get("type")

    def extract_required(self, schema):
        return schema.get("required", [])

    def extract_properties(self, schema):
        return schema.get("properties", {})

    def extract_properties_metadata(self, schema):
       
        properties = self.extract_properties(schema)
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
                key: value for key, value in metadata.items() if value is not None
            }

        return extracted_properties

    def resolve_nested_references(self, schema, swagger_data, resolver):
        properties = self.extract_properties(schema)
        resolved_nested_references = {}

        for property_name, property_details in properties.items():
            resolved = resolver.resolve_schema_ref(property_details, swagger_data)

            if resolved != property_details:
                resolved_nested_references[property_name] = resolved


        return resolved_nested_references
