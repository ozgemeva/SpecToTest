import pytest

from app.api_parser.swagger_parser import SwaggerParser
from tests.unit_tests.mock_data.edge_case_swagger import (
    EDGE_CASE_SWAGGER_EXTRA_UNKNOWN_DATA,
    EDGE_CASE_SWAGGER_MISSING_DATA,
    EDGE_CASE_SWAGGER_PATHS_DATA,
    EDGE_CASE_SWAGGER_UPPERCASE_METHOD_DATA,
)
from tests.unit_tests.mock_data.extract_schema import REQUEST_SCHEMA_DETAILS_DATA
from tests.unit_tests.mock_data.extract_schema_none import REQUEST_SCHEMA_NONE_DETAILS_DATA
from tests.unit_tests.mock_data.invalid_swagger import (
    EMPTY_INVALID_SWAGGER_DATA,
    INVALID_SWAGGER_DATA,
    ISDICT_INVALID_DETAILS_SWAGGER_DATA,
    ISDICT_INVALID_MEHTOD_SWAGGER_DATA,
    ISDICT_INVALID_SWAGGER_DATA,
)
from tests.unit_tests.mock_data.valid_swagger import VALID_SWAGGER_DATA
from tests.unit_tests.mock_data.extract_response_schema import RESPONSE_DETAILS
from tests.unit_tests.mock_data.extract_responce_invalid_schema import RESPONSE_NOT200_DETAILS
from tests.unit_tests.mock_data.extract_responce_invalid_schema import RESPONSE_NOT_DICT_DETAILS

@pytest.fixture
def swagger_body_parameter_response_schema_nondict_detais_data():
    return RESPONSE_NOT_DICT_DETAILS

@pytest.fixture
def swagger_body_parameter_response_schema_not200_details_data():
    return RESPONSE_NOT200_DETAILS

@pytest.fixture
def swagger_body_parameter_request_schema_none_details_data():
    return REQUEST_SCHEMA_NONE_DETAILS_DATA

@pytest.fixture
def swagger_body_paramete_request_schema_detail_data():
    return REQUEST_SCHEMA_DETAILS_DATA

@pytest.fixture
def swagger_body_paramete_response_schema_detail_data():
    return RESPONSE_DETAILS


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
def invalid_swagger_data():
    return INVALID_SWAGGER_DATA

@pytest.fixture
def valid_swagger_data():
    return VALID_SWAGGER_DATA

@pytest.fixture
def empty_swagger_data():
    return EMPTY_INVALID_SWAGGER_DATA

@pytest.fixture
def isdict_swagger_data():
    return ISDICT_INVALID_SWAGGER_DATA

@pytest.fixture
def isdict_method_swagger_data():
    return ISDICT_INVALID_MEHTOD_SWAGGER_DATA

@pytest.fixture
def isdict_details_swagger_data():
    return ISDICT_INVALID_DETAILS_SWAGGER_DATA

# prepared test environment with fixture function
def create_mock_parser(monkeypatch, mock_data):

    def fake_fetch(self):
        return mock_data

    monkeypatch.setattr(SwaggerParser, "fetch_swagger", fake_fetch)
    return SwaggerParser()

@pytest.fixture
def parser_with_valid_mock(monkeypatch, valid_swagger_data):
    return create_mock_parser(monkeypatch, valid_swagger_data)

@pytest.fixture
def parser_with_invalid_mock(monkeypatch, invalid_swagger_data):
    return create_mock_parser(monkeypatch, invalid_swagger_data)

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
def parser_with_extra_unknown_field_mock(monkeypatch, edge_case_extra_unknown_field_data):
    return create_mock_parser(monkeypatch, edge_case_extra_unknown_field_data)

@pytest.fixture
def parser_with_empty_fields_mock(monkeypatch, empty_swagger_data):
    return create_mock_parser(monkeypatch, empty_swagger_data)

@pytest.fixture
def parser_with_nodict_fields_mock(monkeypatch, isdict_swagger_data):
    return create_mock_parser(monkeypatch, isdict_swagger_data)

@pytest.fixture
def parser_with_nodict_method_fields_mock(monkeypatch, isdict_method_swagger_data):
    return create_mock_parser(monkeypatch, isdict_method_swagger_data)

@pytest.fixture
def parser_with_nodict_details_fields_mock(monkeypatch, isdict_details_swagger_data):
    return create_mock_parser(monkeypatch, isdict_details_swagger_data)

@pytest.fixture
def parser_with_extract_request_schema_none_details(monkeypatch,swagger_body_parameter_request_schema_none_details_data):
    return create_mock_parser(monkeypatch,swagger_body_parameter_request_schema_none_details_data)

@pytest.fixture
def parser_with_extract_request_schema_details(monkeypatch,swagger_body_paramete_request_schema_detail_data):
    return create_mock_parser(monkeypatch,swagger_body_paramete_request_schema_detail_data)

@pytest.fixture
def parser_with_extract_response_schema_details(monkeypatch,swagger_body_paramete_response_schema_detail_data):
    return create_mock_parser(monkeypatch,swagger_body_paramete_response_schema_detail_data)

@pytest.fixture
def parser_with_extract_response_schema_not200_details(monkeypatch,swagger_body_parameter_response_schema_not200_details_data):
    return create_mock_parser(monkeypatch,swagger_body_parameter_response_schema_not200_details_data)

@pytest.fixture
def parser_with_extract_response_schema_nondict_details(monkeypatch,swagger_body_parameter_response_schema_nondict_detais_data):
    return create_mock_parser(monkeypatch,swagger_body_parameter_response_schema_nondict_detais_data)