import csv
import datetime
import logging

from config import TIMEZONE


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
      Loads prompt configurations from a CSV file and returns them as a dictionary.

      Args:
          file_path (str): Path to the CSV file.

      Returns:
          dict: A dictionary where each key is a prompt number, and the value contains
          'prompt_template', 'options', and 'instruction' for that prompt.
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
