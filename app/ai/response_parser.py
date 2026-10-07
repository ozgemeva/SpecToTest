import json

# Converts the AI output string into a Python object.
class ResponseParser:
    def parse_response(self, output_text):
        json_resp = json.loads(output_text)
        return json_resp


