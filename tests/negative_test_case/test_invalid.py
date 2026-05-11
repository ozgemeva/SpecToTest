
def test_invalid_methods_are_skipped(parser_with_invalid_mock):
  endpoints = parser_with_invalid_mock.parse_paths()
  assert len(endpoints) == 0, (f"Expected 0 endpoints but got {len(endpoints)}")