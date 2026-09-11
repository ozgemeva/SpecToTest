import pytest

from app.api_parser.swagger_parser import SwaggerParser
from tests.unit_tests.mock_data.phase_1_swagger_mockdata.edge_case_swagger import (
    EDGE_CASE_SWAGGER_EXTRA_UNKNOWN_DATA,
    EDGE_CASE_SWAGGER_MISSING_DATA,
    EDGE_CASE_SWAGGER_PATHS_DATA,
    EDGE_CASE_SWAGGER_UPPERCASE_METHOD_DATA,
)
from tests.unit_tests.mock_data.phase_1_swagger_mockdata.invalid_swagger import (
    EMPTY_INVALID_SWAGGER_DATA,
    INVALID_SWAGGER_DATA,
    ISDICT_INVALID_DETAILS_SWAGGER_DATA,
    ISDICT_INVALID_MEHTOD_SWAGGER_DATA,
    ISDICT_INVALID_SWAGGER_DATA,
)
from tests.unit_tests.mock_data.phase_1_swagger_mockdata.valid_swagger import (
    VALID_SWAGGER_DATA,
)
from tests.unit_tests.mock_data.phase_2_schema_mocktada.extract_request_schema import (
    REQUEST_SCHEMA_DETAILS_DATA,
    REQUEST_SCHEMA_NONE_DETAILS_DATA,
)
from tests.unit_tests.mock_data.phase_2_schema_mocktada.extract_responce_schema import (
    RESPONSE_DETAILS,
    RESPONSE_NOT200_DETAILS,
    RESPONSE_NOT_DICT_DETAILS,
)
from tests.unit_tests.mock_data.phase_2_schema_mocktada.properties_metadata import (
    PROPERTIES_METADATA_WITH_REQUIRED,
    PROPERTIES_METADATA_WITHOUT_REQUIRED,
)


@pytest.fixture
def schema_properties_wit_required():
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
