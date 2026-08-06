import pytest

def test_invalid_nodict_paths(parser_with_nodict_fields_mock):
        with pytest.raises(ValueError,match=r"Invalid Swagger document: 'paths' must be a dictionary",):
                parser_with_nodict_fields_mock.parse_paths()

