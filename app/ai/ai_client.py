import os

from dotenv import load_dotenv
from openai import OpenAI


def api_kontrol_load_env():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        print("OpenAI API key loaded successfully.")
    else:
        print("OpenAI API key not found.")


def create_ai_client():
    load_dotenv()
    client = OpenAI()

    return client