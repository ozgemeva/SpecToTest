import pytest
from app.api_parser.swagger_parser import SwaggerParser

@pytest.fixture
def parser_with_mock(monkeypatch, invalid_swagger_data):

    def fake_fetch(self):
        return invalid_swagger_data

    monkeypatch.setattr(
        SwaggerParser,
        "fetch_swagger",
        fake_fetch
    )

    return SwaggerParser()