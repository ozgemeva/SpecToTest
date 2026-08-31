from app.schema.schema_extractor import SchemaExtractor
from app.schema.schema_resolver import SchemaResolver


class SchemaProcessor:
    def __init__(self):
        self.resolver = SchemaResolver()
        self.extractor = SchemaExtractor()

    def process_schema(self, schema, swagger_data):
        if not schema:
            return None

        resolved_schema = self.resolver.resolve_schema_ref(schema, swagger_data)
        metadata = self.extractor.extract_properties_metadata(resolved_schema)
        nested_references = self.extractor.resolve_nested_references(
            resolved_schema, swagger_data, self.resolver
        )

        return {
            "metadata": metadata,
            "nested_references": nested_references,
        }
