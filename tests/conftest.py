import pytest
from app.api_parser.swagger_parser import SwaggerParser
from tests.mock_data.valid_swagger import VALID_SWAGGER_DATA
from tests.mock_data.invalid_swagger import INVALID_SWAGGER_DATA
from tests.mock_data.edge_case_swagger import EDGE_CASE_SWAGGER_MISSING_DATA
from tests.mock_data.edge_case_swagger import EDGE_CASE_SWAGGER_PATHS_DATA
from tests.mock_data.edge_case_swagger import EDGE_CASE_SWAGGER_UPPERCASE_METHOD_DATA
from tests.mock_data.edge_case_swagger import EDGE_CASE_SWAGGER_EXTRA_UNKNOWN_DATA

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


#prepared test environment with fixture function
def create_mock_parser(monkeypatch, mock_data):

    def fake_fetch(self):
        return mock_data

    monkeypatch.setattr(
        SwaggerParser,
        "fetch_swagger",
        fake_fetch
    )
    return SwaggerParser()

@pytest.fixture
def parser_with_valid_mock(monkeypatch, valid_swagger_data):
    return create_mock_parser(monkeypatch, valid_swagger_data)

@pytest.fixture
def parser_with_invalid_mock(monkeypatch, invalid_swagger_data):
    return create_mock_parser(monkeypatch, invalid_swagger_data)

@pytest.fixture
def parser_with_empty_paths_mock(monkeypatch,edge_case_empty_paths_data):
    return create_mock_parser(monkeypatch,edge_case_empty_paths_data)

@pytest.fixture
def parser_with_missing_fields_mock(monkeypatch,edge_case_missing_fields_data):
    return create_mock_parser(monkeypatch,edge_case_missing_fields_data)

@pytest.fixture
def parser_with_uppercase_method_mock (monkeypatch,edge_case_uppercase_method_data):
    return create_mock_parser(monkeypatch,edge_case_uppercase_method_data)

@pytest.fixture
def parser_with_extra_unknown_field_mock(monkeypatch,edge_case_extra_unknown_field_data):
    return create_mock_parser(monkeypatch,edge_case_extra_unknown_field_data)