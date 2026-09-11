import requests

from app.api_parser.swagger_parser import SwaggerParser


def test_fetch_swagger_from_local_file(tmp_path, mocker):

    swagger_file = tmp_path / "swagger.json"
    swagger_file.write_text("""{"paths": {}}""")

    # URL is fail,it throws connection error instead of requests.get()
    mocker.patch(
        "app.api_parser.swagger_parser.requests.get",
        side_effect=requests.ConnectionError(),
    )

    parser = SwaggerParser()
    parser.source = str(swagger_file)

    result = parser.fetch_swagger()

    assert result == {"paths": {}}, "Failed to load swagger JSON from local file"
