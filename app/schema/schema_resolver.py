"""Resolves direct and array item schema references using Swagger definitions."""


class SchemaResolver:
    # Resolves request/response schema references to the actual schema definition
    def resolve_schema_ref(self, schema, swagger_data):
        if "allOf" in schema:
            merged_schema = {
                "type": schema.get("type", "object"),
                "required": [],
                "properties": {},
            }

            for part in schema["allOf"]:
                resolved_part = self.resolve_schema_ref(part, swagger_data)

                if not resolved_part:
                    continue

                merged_schema["required"].extend(resolved_part.get("required", []))

                merged_schema["properties"].update(resolved_part.get("properties", {}))

                merged_schema["required"] = list(
                    dict.fromkeys(merged_schema["required"])
                )

            return merged_schema

        ref = schema.get("$ref")

        if not ref and schema.get("type") == "array":
            items = schema.get("items", {})
            ref = items.get("$ref")

        if not ref:
            return schema

        model_name = self.get_model_name(ref)
        definitions = self.get_definitions(swagger_data)

        resolved_schema = definitions.get(model_name)

        if not resolved_schema:
            return None

        return self.resolve_schema_ref(resolved_schema, swagger_data)

    def get_definitions(self, swagger_data):
        return swagger_data.get("definitions", {})

    def get_model_name(self, ref):
        # Extracts the model name from the $ref path (e.g. "#/definitions/Pet" -> "Pet")
        return ref.split("/")[-1]
