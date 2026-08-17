class SchemaResolver:
    # Resolves request/response schema references to the actual schema definition
    def resolve_schema_ref(self, schema, swagger_data):
        ref = schema.get("$ref")

        if not ref:
            return schema

        model_name = self.get_model_name(ref)
        definitions = self.get_definitions(swagger_data)

        return definitions.get(model_name)

    def get_definitions(self, swagger_data):
        return swagger_data.get("definitions", {})

    def get_model_name(self, ref):
        # Extracts the model name from the $ref path (e.g. "#/definitions/Pet" -> "Pet")
        return ref.split("/")[-1]
