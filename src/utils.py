import csv
import datetime
from config import TIMEZONE, logging


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
                result.append((index.strip(), specification.strip(), label.strip()))
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


def save_response_to_csv(data: list[tuple]):
    """
    Writes a list of tuples to a CSV file.

    Args:
        data (list): List of tuples (
            ('Test Number', 'Expected Label', 'LLM Result', 'LLM Step by Step Reasoning', 'LLM', 'Prompt Number')
        ).
    """

    now = datetime.datetime.now(TIMEZONE).strftime("%Y-%m-%d-%H:%M:%S")
    try:
        with open(f"results/{now}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                [
                    "Test Number",
                    "Expected Label",
                    "LLM Result",
                    "LLM Step by Step Reasoning",
                    "LLM",
                    "Prompt Number",
                    "Prompt Template",
                    "OPTIONS",
                    "INSTRUCTION",
                ]
            )
            for row in data:
                writer.writerow(row)
    except Exception as e:
        logging.exception(f"An error occurred: {e}")


def get_result_word(expected: str, obtained: str):
    """
    Compare if expected sentence is in obtained
    and return the result word in Streamlit format
    """
    if expected in obtained:
        return ":green[success]"
    return ":red[failed]"


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
