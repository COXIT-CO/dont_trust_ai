import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DEFAULT_LLM_MODEL = os.getenv("DEFAULT_LLM_MODEL")

CSV_FILE_PATH = os.getenv("CSV_FILE_PATH")
