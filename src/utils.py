import csv
import datetime

import asyncio

from config import TIMEZONE, logging, PRICES_PER_1000_TOKEN


def run_async_in_sync(function, *args, **kwargs):
    """
    Function to run the async code within the synchronous context
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(function(*args, **kwargs))


def read_testcases_from_csv(file_path) -> list:
    """
    Reads a CSV file and returns a list of tuples (index, label, specification).

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of tuples (index, label, specification).
    """
    result = []

    try:
        with open(file_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                index, label, specification = row
                result.append((index.strip(), label.strip(), specification.strip()))
    except FileNotFoundError:
        logging.exception(f"File '{file_path}' not found.")
    return result[1:]


def read_prompts_from_csv(file_path) -> list:
    """
    Reads a CSV file and returns a list of tuples (number, prompt_template, options, instruction).

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of tuples (number, prompt_template, options, instruction).
    """
    result = []
    try:
        with open(file_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                number, prompt_template, options, instruction = row
                result.append(
                    (
                        number.strip(),
                        prompt_template.strip(),
                        options.strip(),
                        instruction.strip(),
                    )
                )
    except FileNotFoundError:
        logging.exception(f"File '{file_path}' not found.")
    return result[1:]


def save_response_to_csv(columns: tuple, data: list[tuple], file_path: str = "results"):
    """
    Writes a list of tuples to a CSV file.

    Args:
        data (list): List of tuples
        columns (tuple): Tuple of column names
        file_path (str): Path to the CSV file
    """

    now = datetime.datetime.now(TIMEZONE).strftime("%Y-%m-%d-%H:%M:%S")
    try:
        with open(f"{file_path}/{now}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(columns)
            for row in data:
                writer.writerow(row)
    except Exception as e:
        logging.exception(f"An error occurred: {e}")


def get_prompts_config(file_path: str):
    """
    Create prompts config dictionary from CSV file.
    """
    prompts_config_tuples = read_prompts_from_csv(file_path)
    prompts_config = {
        number: {
            "prompt_template": prompt_template,
            "options": options,
            "instruction": instruction,
        }
        for number, prompt_template, options, instruction in prompts_config_tuples
    }
    return prompts_config


def calculate_llm_call_cost(model_name, input_tokens, output_tokens):
    if model_name not in PRICES_PER_1000_TOKEN:
        return 0

    input_price_per_1000 = PRICES_PER_1000_TOKEN[model_name]["input"]
    output_price_per_1000 = PRICES_PER_1000_TOKEN[model_name]["output"]

    input_cost = (input_tokens / 1000) * input_price_per_1000
    output_cost = (output_tokens / 1000) * output_price_per_1000
    total_cost = input_cost + output_cost

    return round(total_cost, 4)
