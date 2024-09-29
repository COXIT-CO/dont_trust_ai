import logging
import os
import pytz
from datetime import datetime
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_DEFAULT_LLM_MODELS = os.getenv("OPENROUTER_DEFAULT_LLM_MODELS").split(",")

PATH_TO_TESTCASES_CSV_FILE = os.getenv("PATH_TO_TESTCASES_CSV_FILE")
PATH_TO_PROMPT_CSV_FILE = os.getenv("PATH_TO_PROMPT_CSV_FILE")

TIMEZONE_REGION = os.getenv("TIMEZONE_REGION")

TIMEZONE = pytz.timezone(TIMEZONE_REGION)

os.makedirs("results", exist_ok=True)
os.makedirs("deepeval_results", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=f"logs/{datetime.now(TIMEZONE).strftime('%Y_%m_%d_%H:%M:%S')}",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)


def get_client() -> AsyncOpenAI:
    return AsyncOpenAI(
        base_url=OPENROUTER_BASE_URL,
        api_key=OPENROUTER_API_KEY,
    )
