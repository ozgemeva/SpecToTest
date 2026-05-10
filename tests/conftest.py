import pytest
from app.api_parser.swagger_parser import SwaggerParser
    
#prepared test environment with fixture function
@pytest.fixture # fake_swagger_data = fake_swagger_data() 
def parser_with_mock(monkeypatch, valid_swagger_data):
    def fake_fetch(self):
        return valid_swagger_data
  
    #real api closed, mock data opened
    monkeypatch.setattr(SwaggerParser,
                        "fetch_swagger", 
                        fake_fetch)
    return SwaggerParser() #return instance from SwaggerParser

    fake_swagger_data