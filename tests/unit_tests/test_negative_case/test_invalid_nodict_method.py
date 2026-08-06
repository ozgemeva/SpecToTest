import pytest


def test_invalid_nodict_method(parser_with_nodict_method_fields_mock):
    with pytest.raises(
        ValueError, match="Invalid path definition for '/test': expected a dictionary"
    ):
        parser_with_nodict_method_fields_mock.parse_paths()
