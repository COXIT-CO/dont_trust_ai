import os
from openai import AsyncOpenAI
from dotenv import load_dotenv


load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
DEFAULT_LLM_MODEL = os.getenv("DEFAULT_LLM_MODEL")
DEFAULT_LLM_TEMPERATURE = os.getenv("DEFAULT_LLM_TEMPERATURE")
CSV_FILE_PATH = os.getenv("CSV_FILE_PATH")


client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENROUTER_API_KEY,
)

