import pytest
import requests

from app.api_parser.swagger_parser import SwaggerParser


@pytest.mark.parametrize(
    "error_message", ["401 Unauthorized", "404 Not Found", "500 Server Error"]
)
def test_fetch_swagger_falls_back_to_local_file_on_http_error(mocker, error_message):
    mock_response = mocker.Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError(error_message)

    mocker.patch(
        "app.api_parser.swagger_parser.requests.get", return_value=mock_response
    )
    parser = SwaggerParser()

    mocker.patch.object(parser, "fetch_swagger_from_file", return_value={"paths": {}})
    result = parser.fetch_swagger()

    assert result == {"paths": {}}
