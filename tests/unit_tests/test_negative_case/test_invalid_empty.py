import pytest


def test_invalid_empty(parser_with_empty_fields_mock):
    with pytest.raises(
        ValueError,
        match=r"Invalid Swagger document: missing 'paths' field",
    ):
        parser_with_empty_fields_mock.parse_paths()
