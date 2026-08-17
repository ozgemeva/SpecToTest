class SchemaExtractor:

    def extract_type(self, schema):
        return schema.get("type")

    def extract_properties(self, schema):
        properties = schema.get("properties", {})
        for property_name, property_details in properties.items():
            return ("PROPERTY:", property_name), ("DETAILS:", property_details)

    def extract_required(self, schema):
        return schema.get("required")
