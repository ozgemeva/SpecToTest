import pytest

def test_invalid_nodict_paths(parser_with_nodict_details_fields_mock):
        with pytest.raises(ValueError,match=r"Invalid operation 'get' for path '/test': expected a dictionary"):
                parser_with_nodict_details_fields_mock.parse_paths()
