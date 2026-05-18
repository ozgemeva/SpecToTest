import pytest

def test_invalid_nodict(parser_with_nodict_fields_mock):
        with pytest.raises(ValueError,match="Paths must be a dictionary"):
                parser_with_nodict_fields_mock.parse_paths()

