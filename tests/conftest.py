import pytest

from app.api_parser.swagger_parser import SwaggerParser
from app.schema.schema_processor import SchemaProcessor
from tests.unit_tests.mock_data.phase_1_swagger_data_md.edge_case_swagger import (
    EDGE_CASE_SWAGGER_EXTRA_UNKNOWN_DATA,
    EDGE_CASE_SWAGGER_MISSING_DATA,
    EDGE_CASE_SWAGGER_PATHS_DATA,
    EDGE_CASE_SWAGGER_UPPERCASE_METHOD_DATA,
)
from tests.unit_tests.mock_data.phase_1_swagger_data_md.invalid_swagger import (
    EMPTY_INVALID_SWAGGER_DATA,
    INVALID_SWAGGER_DATA,
    ISDICT_INVALID_DETAILS_SWAGGER_DATA,
    ISDICT_INVALID_MEHTOD_SWAGGER_DATA,
    ISDICT_INVALID_SWAGGER_DATA,
)
from tests.unit_tests.mock_data.phase_1_swagger_data_md.valid_swagger import (
    VALID_SWAGGER_DATA,
)
from tests.unit_tests.mock_data.phase_2_schema_md.extract_request_schema import (
    REQUEST_SCHEMA_DETAILS_DATA,
    REQUEST_SCHEMA_NONE_DETAILS_DATA,
)
from tests.unit_tests.mock_data.phase_2_schema_md.extract_responce_schema import (
    RESPONSE_DETAILS,
    RESPONSE_NOT200_DETAILS,
    RESPONSE_NOT_DICT_DETAILS,
)
from tests.unit_tests.mock_data.phase_2_schema_md.process_schema import (
    PROCESS_EMPTY_SCHEMA,
    PROCESS_EXPECTED_METADATA,
    PROCESS_EXPECTED_NESTED,
    PROCESS_SCHEMA,
)
from tests.unit_tests.mock_data.phase_2_schema_md.properties_metadata import (
    PROPERTIES_METADATA,
    PROPERTIES_METADATA_NONE_FIELD,
    PROPERTIES_METADATA_WITH_REQUIRED,
    PROPERTIES_METADATA_WITHOUT_REQUIRED,
)


@pytest.fixture
def schema_process():
    return PROCESS_SCHEMA


@pytest.fixture
def schema_process_expected_nested():
    return PROCESS_EXPECTED_NESTED


@pytest.fixture
def schema_process_expected_metadata():
    return PROCESS_EXPECTED_METADATA


@pytest.fixture
def schema_process_empty_schema():
    return PROCESS_EMPTY_SCHEMA


@pytest.fixture
def schema_properties_with_none_field():
    return PROPERTIES_METADATA_NONE_FIELD


@pytest.fixture
def schema_properties_metadata():
    return PROPERTIES_METADATA


@pytest.fixture
def schema_properties_with_required():
    return PROPERTIES_METADATA_WITH_REQUIRED


@pytest.fixture
def schema_properties_without_required():
    return PROPERTIES_METADATA_WITHOUT_REQUIRED


@pytest.fixture
def schema_response_body_parameter_detail_data():
    return RESPONSE_DETAILS


@pytest.fixture
def schema_response_body_parameter_nondict_detais_data():
    return RESPONSE_NOT_DICT_DETAILS


@pytest.fixture
def schema_response_body_parameter_not200_details_data():
    return RESPONSE_NOT200_DETAILS


@pytest.fixture
def schema_request_body_parameter_none_details_data():
    return REQUEST_SCHEMA_NONE_DETAILS_DATA


@pytest.fixture
def schema_request_body_paramete_detail_data():
    return REQUEST_SCHEMA_DETAILS_DATA


@pytest.fixture
def edge_case_extra_unknown_field_data():
    return EDGE_CASE_SWAGGER_EXTRA_UNKNOWN_DATA


@pytest.fixture
def edge_case_uppercase_method_data():
    return EDGE_CASE_SWAGGER_UPPERCASE_METHOD_DATA


@pytest.fixture
def edge_case_missing_fields_data():
    return EDGE_CASE_SWAGGER_MISSING_DATA


@pytest.fixture
def edge_case_empty_paths_data():
    return EDGE_CASE_SWAGGER_PATHS_DATA


@pytest.fixture
def swagger_data_invalid():
    return INVALID_SWAGGER_DATA


@pytest.fixture
def swagger_data_valid():
    return VALID_SWAGGER_DATA


@pytest.fixture
def swagger_data_empty():
    return EMPTY_INVALID_SWAGGER_DATA


@pytest.fixture
def swagger_data_isdict():
    return ISDICT_INVALID_SWAGGER_DATA


@pytest.fixture
def swagger_data_isdict_method():
    return ISDICT_INVALID_MEHTOD_SWAGGER_DATA


@pytest.fixture
def swagger_data_isdict_details():
    return ISDICT_INVALID_DETAILS_SWAGGER_DATA


# prepared test environment with fixture function
def create_mock_parser(monkeypatch, mock_data):

    def fake_fetch(self):
        return mock_data

    monkeypatch.setattr(SwaggerParser, "fetch_swagger", fake_fetch)
    return SwaggerParser()


@pytest.fixture
def parser_with_valid_mock(monkeypatch, swagger_data_valid):
    return create_mock_parser(monkeypatch, swagger_data_valid)


@pytest.fixture
def parser_with_invalid_mock(monkeypatch, swagger_data_invalid):
    return create_mock_parser(monkeypatch, swagger_data_invalid)


@pytest.fixture
def parser_with_empty_paths_mock(monkeypatch, edge_case_empty_paths_data):
    return create_mock_parser(monkeypatch, edge_case_empty_paths_data)


@pytest.fixture
def parser_with_missing_fields_mock(monkeypatch, edge_case_missing_fields_data):
    return create_mock_parser(monkeypatch, edge_case_missing_fields_data)


@pytest.fixture
def parser_with_uppercase_method_mock(monkeypatch, edge_case_uppercase_method_data):
    return create_mock_parser(monkeypatch, edge_case_uppercase_method_data)


@pytest.fixture
def parser_with_extra_unknown_field_mock(
    monkeypatch, edge_case_extra_unknown_field_data
):
    return create_mock_parser(monkeypatch, edge_case_extra_unknown_field_data)


@pytest.fixture
def parser_with_empty_fields_mock(monkeypatch, swagger_data_empty):
    return create_mock_parser(monkeypatch, swagger_data_empty)


@pytest.fixture
def parser_with_nodict_fields_mock(monkeypatch, swagger_data_isdict):
    return create_mock_parser(monkeypatch, swagger_data_isdict)


@pytest.fixture
def parser_with_nodict_method_fields_mock(monkeypatch, swagger_data_isdict_method):
    return create_mock_parser(monkeypatch, swagger_data_isdict_method)


@pytest.fixture
def parser_with_nodict_details_fields_mock(monkeypatch, swagger_data_isdict_details):
    return create_mock_parser(monkeypatch, swagger_data_isdict_details)


# Creates a SchemaProcessor with mocked resolver and extractor dependencies.
@pytest.fixture
def processor_with_schema_mock(
    monkeypatch,
    schema_process,
    schema_process_expected_nested,
    schema_process_expected_metadata,
):
    processor = SchemaProcessor()

    def fake_resolve_schema_ref(schema, swagger_data):
        return schema_process

    def fake_resolve_nested_references(resolved_schema, swagger_data, resolver):
        return schema_process_expected_nested

    def fake_extract_properties_metadata(resolved_schema):
        return schema_process_expected_metadata

    monkeypatch.setattr(
        processor.resolver,
        "resolve_schema_ref",
        fake_resolve_schema_ref,
    )
    monkeypatch.setattr(
        processor.extractor,
        "extract_properties_metadata",
        fake_extract_properties_metadata,
    )
    monkeypatch.setattr(
        processor.extractor,
        "resolve_nested_references",
        fake_resolve_nested_references,
    )

    return processor
