import logging
import os
import pytz
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_DEFAULT_LLM_MODELS = os.getenv("OPENROUTER_DEFAULT_LLM_MODELS").split(",")

PATH_TO_TESTCASES_CSV_FILE = os.getenv("PATH_TO_TESTCASES_CSV_FILE")
PATH_TO_PROMPT_CSV_FILE = os.getenv("PATH_TO_PROMPT_CSV_FILE")

TIMEZONE_REGION = os.getenv("TIMEZONE_REGION")
TIMEZONE = pytz.timezone(TIMEZONE_REGION)

# Directories creation
os.makedirs("results", exist_ok=True)
os.makedirs("deepeval_results", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=f"logs/{datetime.now(TIMEZONE).strftime('%Y_%m_%d_%H:%M:%S')}",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)


# Constants for manual deepeval testing
DEFAULT_INPUT_COL_NAME = "Specification"
DEFAULT_ACTUAL_OUTPUT_COL_NAME = "LLM Response"
DEFAULT_EXPECTED_OUTPUT_COL_NAME = "Expected Result"
DEFAULT_CONTEXT_COL_NAME = "Prompt"
DEFAULT_ADDITIONAL_METADATA_COL_NAME = "Testcase"

# Input configuration of dataframe for deepeval manual testing
DEFAULT_MANUAL_TESTING_CONFIG = {
    "input_col_name": DEFAULT_INPUT_COL_NAME,
    "actual_output_col_name": DEFAULT_ACTUAL_OUTPUT_COL_NAME,
    "expected_output_col_name": DEFAULT_EXPECTED_OUTPUT_COL_NAME,
    "context_col_name": DEFAULT_CONTEXT_COL_NAME,
    "additional_metadata_col_name": DEFAULT_ADDITIONAL_METADATA_COL_NAME,
}

# CSV HEADERS FOR SAVING
CSV_HEADERS_DEEPEVAL_TESTING = (
    "Testcase",
    "Prompt",
    "Specification",
    "Expected Result",
    "LLM Response",
    "LLM Model",
    "Response_id",
)
CSV_HEADERS_PROMPT_TESTING = (
    "Testcase",
    "Expected Label",
    "LLM Result",
    "LLM Step by Step Reasoning",
    "Prompt Template",
    "INSTRUCTION",
    "OPTIONS",
    "LLM",
    "Prompt Number",
)

# Default setting for llm call with frameworks monitoring
DEFAULT_PROMPT_FOR_MONITORING = "Prompt GPT"
DEFAULT_LLM_MODEL_FOR_MONITORING = "openai/gpt-4o-2024-08-06"

# Token price configuration
PRICES_PER_1000_TOKEN = {
    'openai/gpt-4o-2024-05-13': {'input': 0.005, 'output': 0.015},
    'openai/gpt-4o-2024-08-06': {'input': 0.0025, 'output': 0.01},
    'anthropic/claude-3.5-sonnet-2024-06-20': {'input': 0.003, 'output': 0.015},
    'qwen/qwen-2-72b-instruct': {'input': 0.00034, 'output': 0.00039}
}



