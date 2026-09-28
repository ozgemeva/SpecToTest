import os

from dotenv import load_dotenv
from openai import OpenAI


class LlmClient:

    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key not found.")
        self.client = OpenAI(api_key=api_key)

    # Sends a prompt to the LLM and returns the generated response.
    def send_prompt(self, prompt):
        response = self.client.responses.create(
            model="gpt-5.6-luna",
            input=prompt,
        )
        return response.output_text
