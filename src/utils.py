import csv
from difflib import SequenceMatcher


def read_csv_to_tuples(file_path):
    """
    Reads a CSV file and returns a list of tuples (specification, expected_result).

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of tuples (specification, expected_result).
    """
    result = []
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter='|')
            for row in reader:
                specification, expected_result = row
                result.append((specification.strip(), expected_result.strip()))
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        for r in result:
            print(r)
    return result

def write_tuples_to_csv(file_path, data):
    """
    Writes a list of tuples (specification, expected_result) to a CSV file with '|' as the delimiter.

    Args:
        file_path (str): Path to the CSV file.
        data (list): List of tuples (specification, expected_result).
    """
    try:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')
            for item in data:
                writer.writerow(item)
    except Exception as e:
        print(f"An error occurred: {e}")


def similarity_percentage(sentence1, sentence2):
    """
    Calculates the similarity percentage between two sentences.

    Args:
        sentence1 (str): The first sentence.
        sentence2 (str): The second sentence.

    Returns:
        float: Similarity percentage between the two sentences.
    """
    matcher = SequenceMatcher(None, sentence1, sentence2)
    return round(matcher.ratio() * 100, 2)
