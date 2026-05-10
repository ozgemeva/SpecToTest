import pytest
from app.api_parser.swagger_parser import SwaggerParser
from tests.mock_data.valid_swagger import VALID_SWAGGER_DATA
from tests.mock_data.invalid_swagger import INVALID_SWAGGER_DATA

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